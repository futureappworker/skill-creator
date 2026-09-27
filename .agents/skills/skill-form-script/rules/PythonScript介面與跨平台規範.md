# Rule 1 - 明確命令列介面

- Script 的外部輸入必須透過具名命令列參數、標準輸入或兩者提供。
- 具有兩個以上輸入時，應該使用 `argparse` 定義參數名稱、型別與說明。
- 必要輸入必須標記為必要，不得在缺少輸入時使用隱含預設值繼續執行。
- Script 不得要求執行者修改程式碼常數才能提供輸入。

## Good Example

- 輸入檔與輸出檔都有明確的具名參數，缺少時會由解析器回報。

```python
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--input", required=True)
parser.add_argument("--output", required=True)
args = parser.parse_args()
```

## Bad Example

- 輸入與輸出路徑寫死在程式碼中，呼叫端無法透過執行介面指定。

```python
input_path = "/Users/ben/data/input.json"
output_path = "/Users/ben/data/output.json"
```

# Rule 2 - 輸出與錯誤契約

- 成功執行必須回傳 exit code `0`。
- 輸入錯誤、處理失敗或未完成預期結果時，必須回傳非零 exit code。
- 供後續流程使用的結果必須寫入明確指定的輸出檔或標準輸出。
- 錯誤訊息必須寫入標準錯誤，並指出失敗的輸入或操作。
- Script 不得只輸出無法由呼叫端判斷成功與否的描述。

## Good Example

- 結果與錯誤使用不同串流，呼叫端也能透過 exit code 判斷結果。

```python
import json
import sys

try:
    print(json.dumps({"status": "ok"}))
except OSError as error:
    print(f"cannot write result: {error}", file=sys.stderr)
    raise SystemExit(1)
```

## Bad Example

- 例外被忽略且仍以成功狀態結束，呼叫端無法辨識失敗。

```python
try:
    create_report()
except Exception:
    print("done")
```

# Rule 3 - 跨平台路徑

- Python 程式碼中的檔案路徑必須使用 `pathlib.Path` 或等效的跨平台 API 組合。
- Skill 內部資源路徑必須相對於 Script 自身位置解析。
- 呼叫端提供的相對輸入與輸出路徑必須依命令執行目錄解析，並在說明中保持一致。
- 路徑不得包含開發者電腦的絕對路徑。
- Script 不得使用手動串接的 `/` 或 `\` 建立路徑。

## Good Example

- 內部資源從 `__file__` 尋找，不受 Windows 或 POSIX 路徑分隔符影響。

```python
from pathlib import Path

script_dir = Path(__file__).resolve().parent
schema_path = script_dir / "assets" / "schema.json"
```

## Bad Example

- 路徑固定為特定使用者的 macOS 目錄，無法在其他電腦執行。

```python
schema_path = "/Users/ben/skill/scripts/assets/schema.json"
```

# Rule 4 - 非互動式執行

- Script 必須能在沒有人工輸入的代理執行環境中完成。
- Script 不得使用 `input()`、互動式選單或 GUI 對話框取得必要資料。
- 需要確認的破壞性操作必須使用明確的命令列旗標授權。
- 缺少破壞性操作的授權旗標時，Script 必須停止且不得修改資料。

## Good Example

- 刪除操作只有在呼叫端明確傳入旗標後才執行。

```python
parser.add_argument("--confirm-delete", action="store_true")
args = parser.parse_args()
if not args.confirm_delete:
    parser.error("--confirm-delete is required")
```

## Bad Example

- Script 執行到一半等待人工回答，使 AI 無法可靠自動執行。

```python
if input("Delete all generated files? [y/N] ") == "y":
    delete_files()
```

# Rule 5 - 副作用邊界

- Script 必須只修改命令列介面明確指定的檔案、目錄或外部資源。
- Script 具有破壞性副作用時，必須提供 `--dry-run` 或等效的唯讀預覽模式。
- `--dry-run` 必須列出預計執行的變更且不得產生實際副作用。
- Script 不得修改 Skill 未授權的專案檔案、使用者設定或系統環境。

## Good Example

- 呼叫端可先檢查同一組輸入將造成的變更，再決定是否正式執行。

```text
uv run --script scripts/cleanup.py --target build --dry-run
```

## Bad Example

- Script 啟動後立即刪除目前目錄，沒有指定範圍或預覽機制。

```python
from pathlib import Path
from shutil import rmtree

rmtree(Path.cwd())
```
