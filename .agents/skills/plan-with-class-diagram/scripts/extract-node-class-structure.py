# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "tree-sitter>=0.23.2,<0.24",
#   "tree-sitter-javascript==0.23.1",
#   "tree-sitter-typescript==0.23.2",
# ]
# ///

"""從 Node.js 原始碼擷取入口類別向外、數量有上限的類別結構。"""

import json
import sys
from argparse import ArgumentParser, Namespace
from dataclasses import dataclass
from pathlib import Path

import tree_sitter_javascript
import tree_sitter_typescript
from tree_sitter import Language, Node, Parser

SOURCE_SUFFIXES = {".js", ".mjs", ".cjs", ".jsx", ".ts", ".tsx"}
SKIPPED_DIRECTORIES = {"node_modules", "dist", "build", "coverage", ".git"}
BUILTIN_TYPE_NAMES = frozenset(
    {
        "string",
        "number",
        "boolean",
        "any",
        "unknown",
        "void",
        "never",
        "null",
        "undefined",
        "object",
        "symbol",
        "bigint",
        "Object",
        "String",
        "Number",
        "Boolean",
        "Symbol",
        "BigInt",
        "Promise",
        "Array",
        "ReadonlyArray",
        "Record",
        "Map",
        "Set",
        "WeakMap",
        "WeakSet",
        "Partial",
        "Required",
        "Pick",
        "Omit",
        "Readonly",
        "Exclude",
        "Extract",
        "NonNullable",
        "ReturnType",
        "Parameters",
        "ConstructorParameters",
        "InstanceType",
        "Date",
        "Error",
        "RegExp",
        "Function",
        "PromiseLike",
        "Iterable",
        "Iterator",
        "AsyncIterable",
        "AsyncIterator",
    }
)
DECLARATION_KINDS = {
    "class_declaration": "class",
    "abstract_class_declaration": "class",
    "interface_declaration": "interface",
}
REFERENCE_STOP_NODES = set(DECLARATION_KINDS) | {
    "statement_block",
    "type_parameters",
    "enum_declaration",
    "type_alias_declaration",
}


def _text(source: bytes, node: Node) -> str:
    return source[node.start_byte : node.end_byte].decode("utf-8")


def _unique(names: list[str]) -> list[str]:
    seen: set[str] = set()
    unique: list[str] = []
    for name in names:
        if name in seen:
            continue
        seen.add(name)
        unique.append(name)
    return unique


def _without_builtins(names: list[str]) -> list[str]:
    return [name for name in names if name not in BUILTIN_TYPE_NAMES]


@dataclass(frozen=True)
class ExtractionRequest:
    root: Path
    entry: str
    entry_file: Path | None
    max_classes: int


@dataclass(frozen=True)
class ParsedDeclaration:
    name: str
    kind: str
    file: Path
    base_types: list[str]
    implemented_types: list[str]
    type_references: list[str]


@dataclass(frozen=True)
class ClassRecord:
    name: str
    kind: str
    file: str
    extends_names: list[str]
    implements_names: list[str]


@dataclass(frozen=True)
class RelationRecord:
    source: str
    target: str
    kind: str


class ClassStructure:
    def __init__(
        self,
        entry: str,
        max_classes: int,
        truncated: bool,
        classes: list[ClassRecord],
        relationships: list[RelationRecord],
    ) -> None:
        self.entry = entry
        self.max_classes = max_classes
        self.truncated = truncated
        self._classes = classes
        self._relationships = relationships

    def to_json(self) -> str:
        payload = {
            "language": "node",
            "entry": self.entry,
            "maxClasses": self.max_classes,
            "truncated": self.truncated,
            "classes": [
                {
                    "name": record.name,
                    "kind": record.kind,
                    "file": record.file,
                    "extends": record.extends_names,
                    "implements": record.implements_names,
                }
                for record in self._classes
            ],
            "relationships": [
                {
                    "from": relation.source,
                    "to": relation.target,
                    "kind": relation.kind,
                }
                for relation in self._relationships
            ],
        }
        return json.dumps(payload, ensure_ascii=False, indent=2)


class StructureExtractionError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


class NodeSyntaxParser:
    def __init__(self) -> None:
        self._javascript = Parser(Language(tree_sitter_javascript.language()))
        self._typescript = Parser(Language(tree_sitter_typescript.language_typescript()))
        self._tsx = Parser(Language(tree_sitter_typescript.language_tsx()))

    def parse_file(self, path: Path) -> list[ParsedDeclaration]:
        source = path.read_bytes()
        tree = self._parser_for(path).parse(source)
        declarations: list[ParsedDeclaration] = []
        self._collect_declarations(source, tree.root_node, path, declarations)
        return declarations

    def _parser_for(self, path: Path) -> Parser:
        if path.suffix == ".ts":
            return self._typescript
        if path.suffix == ".tsx":
            return self._tsx
        return self._javascript

    def _collect_declarations(
        self,
        source: bytes,
        node: Node,
        path: Path,
        declarations: list[ParsedDeclaration],
    ) -> None:
        kind = DECLARATION_KINDS.get(node.type)
        if kind is not None:
            declaration = self._parse_declaration(source, node, path, kind)
            if declaration is not None:
                declarations.append(declaration)
        for child in node.children:
            self._collect_declarations(source, child, path, declarations)

    def _parse_declaration(
        self,
        source: bytes,
        node: Node,
        path: Path,
        kind: str,
    ) -> ParsedDeclaration | None:
        name_node = node.child_by_field_name("name")
        if name_node is None:
            return None
        base_types, implemented_types = self._heritage(source, node)
        return ParsedDeclaration(
            name=_text(source, name_node),
            kind=kind,
            file=path,
            base_types=base_types,
            implemented_types=implemented_types,
            type_references=self._type_references(source, node),
        )

    def _heritage(self, source: bytes, node: Node) -> tuple[list[str], list[str]]:
        base_types: list[str] = []
        implemented_types: list[str] = []
        for child in node.children:
            if child.type == "class_heritage":
                nested_bases, nested_implemented = self._heritage(source, child)
                base_types.extend(nested_bases)
                implemented_types.extend(nested_implemented)
            elif child.type in {"extends_clause", "extends_type_clause"}:
                base_types.extend(self._collect_names(source, child))
            elif child.type == "implements_clause":
                implemented_types.extend(self._collect_names(source, child))
            elif node.type == "class_heritage" and child.is_named:
                base_types.extend(self._collect_names(source, child))
        return _unique(base_types), _unique(implemented_types)

    def _type_references(self, source: bytes, node: Node) -> list[str]:
        body = node.child_by_field_name("body")
        if body is None:
            return []
        names: list[str] = []

        def visit(current: Node) -> None:
            if current.type in REFERENCE_STOP_NODES:
                return
            if current.type == "type_annotation":
                names.extend(self._collect_names(source, current))
                return
            for child in current.children:
                visit(child)

        visit(body)
        return _unique(names)

    def _collect_names(self, source: bytes, node: Node) -> list[str]:
        names: list[str] = []

        def visit(current: Node) -> None:
            if current.type in {
                "type_identifier",
                "identifier",
                "predefined_type",
                "property_identifier",
            }:
                names.append(_text(source, current))
                return
            if current.type in {
                "nested_type_identifier",
                "nested_identifier",
                "member_expression",
            }:
                name_node = current.child_by_field_name("name")
                if name_node is None:
                    name_node = current.child_by_field_name("property")
                if name_node is not None:
                    names.append(_text(source, name_node))
                return
            if current.type == "generic_type":
                name_node = current.child_by_field_name("name")
                if name_node is not None:
                    visit(name_node)
                arguments = current.child_by_field_name("type_arguments")
                if arguments is not None:
                    visit(arguments)
                return
            for child in current.children:
                if child.is_named:
                    visit(child)

        visit(node)
        return names


class DeclarationFinder:
    def __init__(self, parser: NodeSyntaxParser) -> None:
        self._parser = parser
        self._root: Path | None = None
        self._declarations: list[ParsedDeclaration] | None = None

    def set_root(self, root: Path) -> None:
        self._root = root
        self._declarations = None

    def find(self, name: str, entry_file: Path | None) -> list[ParsedDeclaration]:
        if self._root is None:
            raise StructureExtractionError("尚未設定專案根目錄")
        matches = [
            declaration
            for declaration in self._load_declarations()
            if declaration.name == name
        ]
        if entry_file is None:
            return matches
        return [
            declaration
            for declaration in matches
            if self._matches_entry_file(declaration.file, entry_file)
        ]

    def _load_declarations(self) -> list[ParsedDeclaration]:
        if self._declarations is None:
            declarations: list[ParsedDeclaration] = []
            for path in self._source_files():
                declarations.extend(self._parser.parse_file(path))
            self._declarations = declarations
        return self._declarations

    def _source_files(self) -> list[Path]:
        if self._root is None:
            return []
        files: list[Path] = []

        def walk(directory: Path) -> None:
            for child in sorted(directory.iterdir(), key=lambda item: item.name):
                if child.is_symlink():
                    continue
                if child.is_dir():
                    if child.name in SKIPPED_DIRECTORIES:
                        continue
                    walk(child)
                elif child.is_file() and child.suffix in SOURCE_SUFFIXES:
                    files.append(child)

        walk(self._root)
        return files

    def _matches_entry_file(self, file_path: Path, entry_file: Path) -> bool:
        if self._root is None:
            return False
        resolved_file = file_path.resolve()
        relative = resolved_file.relative_to(self._root.resolve()).as_posix()
        if relative == entry_file.as_posix():
            return True
        if entry_file.is_absolute():
            return resolved_file == entry_file.resolve()
        cwd_candidate = (Path.cwd() / entry_file).resolve()
        root_candidate = (self._root / entry_file).resolve()
        return resolved_file in {cwd_candidate, root_candidate}


class ClassStructureExtractor:
    def __init__(self) -> None:
        self._parser = NodeSyntaxParser()
        self._finder = DeclarationFinder(self._parser)

    def extract(self, request: ExtractionRequest) -> ClassStructure:
        self._finder.set_root(request.root)
        matches = self._finder.find(request.entry, request.entry_file)
        if not matches:
            location = ""
            if request.entry_file is not None:
                location = f"（{request.entry_file.as_posix()}）"
            raise StructureExtractionError(f"找不到類別或介面：{request.entry}{location}")
        if len(matches) > 1:
            candidates = "\n".join(
                declaration.file.resolve().relative_to(request.root.resolve()).as_posix()
                for declaration in matches
            )
            raise StructureExtractionError(
                f"類別或介面 {request.entry} 有多個宣告，請用 --entry-file 指定其中一個：\n{candidates}"
            )
        selected, truncated = self._walk(matches[0], request.max_classes)
        records = [
            ClassRecord(
                name=declaration.name,
                kind=declaration.kind,
                file=declaration.file.resolve().relative_to(request.root.resolve()).as_posix(),
                extends_names=_without_builtins(declaration.base_types),
                implements_names=_without_builtins(declaration.implemented_types),
            )
            for declaration in selected
        ]
        included_names = {record.name for record in records}
        relationships: list[RelationRecord] = []
        seen: set[tuple[str, str, str]] = set()
        for declaration, record in zip(selected, records, strict=True):
            for target in record.extends_names:
                self._add_relation(
                    relationships,
                    seen,
                    included_names,
                    record.name,
                    target,
                    "extends",
                )
            for target in record.implements_names:
                self._add_relation(
                    relationships,
                    seen,
                    included_names,
                    record.name,
                    target,
                    "implements",
                )
            for target in _without_builtins(declaration.type_references):
                self._add_relation(
                    relationships,
                    seen,
                    included_names,
                    record.name,
                    target,
                    "dependency",
                )
        return ClassStructure(
            entry=request.entry,
            max_classes=request.max_classes,
            truncated=truncated,
            classes=records,
            relationships=relationships,
        )

    def _walk(
        self,
        start: ParsedDeclaration,
        max_classes: int,
    ) -> tuple[list[ParsedDeclaration], bool]:
        selected: list[ParsedDeclaration] = []
        frontier = [start]
        seen = {self._key(start)}
        truncated = False
        while frontier and len(selected) < max_classes:
            current = frontier.pop(0)
            selected.append(current)
            for neighbor in self._neighbors(current):
                key = self._key(neighbor)
                if key in seen:
                    continue
                if len(selected) + len(frontier) >= max_classes:
                    truncated = True
                    continue
                seen.add(key)
                frontier.append(neighbor)
        return selected, truncated

    def _neighbors(self, declaration: ParsedDeclaration) -> list[ParsedDeclaration]:
        names = _unique(
            _without_builtins(
                [
                    *declaration.base_types,
                    *declaration.implemented_types,
                    *declaration.type_references,
                ]
            )
        )
        neighbors: list[ParsedDeclaration] = []
        for name in names:
            matches = self._finder.find(name, None)
            if len(matches) != 1:
                continue
            neighbors.append(matches[0])
        return neighbors

    def _add_relation(
        self,
        relationships: list[RelationRecord],
        seen: set[tuple[str, str, str]],
        included_names: set[str],
        source: str,
        target: str,
        kind: str,
    ) -> None:
        if target not in included_names:
            return
        identity = (source, target, kind)
        if identity in seen:
            return
        seen.add(identity)
        relationships.append(RelationRecord(source=source, target=target, kind=kind))

    def _key(self, declaration: ParsedDeclaration) -> tuple[str, str]:
        return (str(declaration.file.resolve()), declaration.name)


class Cli:
    def run(self, argv: list[str]) -> int:
        arguments = self._parse_arguments(argv)
        root = Path(arguments.root)
        if not root.is_absolute():
            root = Path.cwd() / root
        root = root.resolve()
        entry_file = Path(arguments.entry_file) if arguments.entry_file else None
        try:
            self._validate(arguments.entry, arguments.max_classes, root)
            request = ExtractionRequest(
                root=root,
                entry=arguments.entry,
                entry_file=entry_file,
                max_classes=arguments.max_classes,
            )
            extractor = ClassStructureExtractor()
            structure = extractor.extract(request)
        except StructureExtractionError as error:
            print(error.message, file=sys.stderr)
            return 1
        print(structure.to_json())
        return 0

    def _validate(self, entry: str, max_classes: int, root: Path) -> None:
        if not entry:
            raise StructureExtractionError("必須提供入口類別")
        if max_classes < 1:
            raise StructureExtractionError("--max-classes 必須是大於 0 的整數")
        if not root.is_dir():
            raise StructureExtractionError(f"專案根目錄不存在：{root}")

    def _parse_arguments(self, argv: list[str]) -> Namespace:
        parser = ArgumentParser(
            description="從 Node.js 原始碼擷取入口類別向外的類別結構。",
        )
        parser.add_argument("--root", required=True, help="專案根目錄")
        parser.add_argument("--entry", required=True, help="入口類別或介面名稱")
        parser.add_argument(
            "--entry-file",
            help="入口宣告所在檔案。相對路徑可相對於目前工作目錄或 --root。",
        )
        parser.add_argument(
            "--max-classes",
            type=int,
            default=30,
            help="最多收錄的類別數量，預設 30",
        )
        return parser.parse_args(argv)


def main() -> int:
    return Cli().run(sys.argv[1:])


if __name__ == "__main__":
    raise SystemExit(main())
