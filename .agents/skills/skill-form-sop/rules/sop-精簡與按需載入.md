# Rule 1 - SOP 內容精簡

- SOP 必須只保留執行流程所需的步驟。
- 詳細約束、判斷標準與 Example 必須放在對應的 Rule File。
- SOP 不得重述已由 Rule File 定義的規則內容。
- SOP 不得加入不影響執行順序的背景說明。

## Good Example

- SOP 只指出載入與撰寫行為，沒有重述格式規則。

```markdown
## Phase 1: 撰寫內容

1. Read [格式規範](rules/格式規範.md)並取得撰寫要求。
2. Write 依已載入規範撰寫目標檔案。
```

## Bad Example

- SOP 在步驟中重述標題、編號及 Example 等詳細格式規則。

```markdown
## Phase 1: 撰寫內容

1. Read [格式規範](rules/格式規範.md)並記住標題必須編號、每條規則必須提供 Good Example 與 Bad Example、Example 必須使用 Code Section。
2. Write 依已載入規範撰寫目標檔案。
```

# Rule 2 - Rule File 只在 Read 步驟提名

- Rule File 的名稱或路徑必須只出現在載入該檔案的 `Read` 步驟。
- `Write`、`Think` 與 `Delegate` 步驟不得提名 Rule File 的名稱或路徑。
- Rule File 載入後，後續步驟必須使用「已載入規範」指稱其內容。

## Good Example

- Rule File 只在 Read 步驟提名，Write 步驟使用「已載入規範」。

```markdown
## Phase 1: 撰寫內容

1. Read [格式規範](rules/格式規範.md)並取得撰寫要求。
2. Write 依已載入規範撰寫目標檔案。
```

## Bad Example

- Write 步驟再次提名已在 Read 步驟載入的 Rule File。

```markdown
## Phase 1: 撰寫內容

1. Read [格式規範](rules/格式規範.md)並取得撰寫要求。
2. Write 依 [格式規範](rules/格式規範.md)撰寫目標檔案。
```

# Rule 3 - Rule File 按需載入

- Rule File 必須在首次需要其內容時載入，且載入步驟必須與首次使用步驟位於同一個 Phase。
- 載入必須使用 `Read` 步驟，且必須排在該 Phase 中首次使用此 Rule File 的步驟之前。
- SOP 不得為載入 Rule File 單獨建立 Phase。
- SOP 不得在尚未需要規範內容時預先載入 Rule File。
- SOP 不得集中載入後續不同 Phase 才需要的 Rule File。

## Good Example

- 格式規範在撰寫 Phase 內、寫入步驟之前才載入，沒有單獨的載入 Phase。

```markdown
## Phase 1: 讀取需求

1. Read 讀取目標需求並取得內容範圍。

## Phase 2: 撰寫內容

1. Read [格式規範](rules/格式規範.md)並取得撰寫要求。
2. Write 依已載入規範撰寫目標檔案。
```

## Bad Example

- 格式規範被拆成專用的載入 Phase，且在進入撰寫之前就預先載入。

```markdown
## Phase 1: 載入格式規範

1. Read [格式規範](rules/格式規範.md)並取得撰寫要求。

## Phase 2: 讀取需求

1. Read 讀取目標需求並取得內容範圍。

## Phase 3: 撰寫內容

1. Write 依已載入規範撰寫目標檔案。
```

# Rule 4 - Rule File 不得重複載入

- 同一次 SOP 執行中，每個 Rule File 必須只載入一次。
- Rule File 載入後，後續 Phase 不得再次讀取相同 Rule File。
- 需要沿用規範內容的步驟必須使用已載入的內容。

## Good Example

- 格式規範只在撰寫 Phase 載入一次，檢查階段沿用已載入規範。

```markdown
## Phase 1: 撰寫內容

1. Read [格式規範](rules/格式規範.md)並取得撰寫要求。
2. Write 依已載入規範撰寫目標檔案。

## Phase 2: 檢查內容

1. Read 依已載入規範檢查目標檔案。
```

## Bad Example

- 檢查階段再次載入已讀取過的格式規範。

```markdown
## Phase 1: 撰寫內容

1. Read [格式規範](rules/格式規範.md)並取得撰寫要求。
2. Write 依已載入規範撰寫目標檔案。

## Phase 2: 檢查內容

1. Read [格式規範](rules/格式規範.md)並檢查目標檔案。
```

# Rule 5 - Rule File 分別載入

- 每個 `Read` 步驟必須只載入一個 Rule File。
- 同一 Phase 需要載入多個 Rule File 時，必須使用不同的 `Read` 步驟分別載入。
- SOP 不得要求讀取整個 `rules/` 目錄或未明確提名的全部 Rule File。

## Good Example

- 兩個 Rule File 在使用它們的 Phase 內，以兩個 Read 步驟分別載入。

```markdown
## Phase 1: 撰寫內容

1. Read [格式規範](rules/格式規範.md)並取得結構要求。
2. Read [品質規範](rules/品質規範.md)並取得內容要求。
3. Write 依已載入規範撰寫目標檔案。
```

## Bad Example

- 單一步驟要求載入整個 rules 目錄，無法判斷實際需要哪個 Rule File。

```markdown
## Phase 1: 撰寫內容

1. Read 讀取 `rules/` 目錄中的全部 Rule File。
2. Write 依已載入規範撰寫目標檔案。
```
