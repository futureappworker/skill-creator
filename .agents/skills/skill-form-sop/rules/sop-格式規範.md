# Rule 1 - SOP 標題

- Skill 的流程區塊必須使用 `# SOP` 作為標題。
- 一份 `SKILL.md` 不得包含兩個以上的 `# SOP` 標題。

## Good Example

- 流程區塊使用唯一的 `# SOP` 標題。

```markdown
# SOP
```

## Bad Example

- 相同流程區塊使用非規定的標題。

```markdown
# Workflow
```

# Rule 2 - Phase 標題與編號

- 每個階段必須使用 `## Phase N: 階段名` 作為標題。
- Phase 編號必須從 1 開始，並依執行順序連續遞增。
- 階段名必須描述該 Phase 的單一目的。

## Good Example

- Phase 從 1 開始連續編號，且階段名描述該 Phase 的單一目的。

```markdown
## Phase 1: 撰寫內容

## Phase 2: 檢查內容
```

## Bad Example

- Phase 從 2 開始且跳號，階段名也未描述目的。

```markdown
## Phase 2: 開始

## Phase 4: 繼續
```

# Rule 3 - Phase 單一目的

- 一個 Phase 必須只處理一個目的。
- 不同目的的步驟必須拆分至不同 Phase。
- 載入本 Phase 所需 Rule File 的 `Read` 步驟屬於該目的，不得為此單獨建立 Phase。
- Phase 內可以包含一個以上服務於同一目的的子步驟。
- 同一 Phase 的子步驟必須從 1 開始，並依執行順序連續遞增。

## Good Example

- 載入撰寫所需規範與撰寫都服務於撰寫內容這一個目的。

```markdown
## Phase 1: 撰寫內容

1. Read [格式規範](rules/格式規範.md)並取得撰寫要求。
2. Write 依已載入規範撰寫目標檔案。
```

## Bad Example

- 同一 Phase 同時處理撰寫與檢查兩個目的。

```markdown
## Phase 1: 撰寫內容

1. Read [格式規範](rules/格式規範.md)並取得撰寫要求。
2. Write 依已載入規範撰寫目標檔案。
3. Read 依已載入規範檢查目標檔案並列出不符合項目。
```

# Rule 4 - 步驟格式

- Phase 內的步驟必須使用有序清單。
- 每個步驟必須以允許的動詞開頭。
- 步驟動詞與行為描述之間必須保留一個空格。

## Good Example

- 步驟使用有序清單，並以動詞及一個空格開頭。

```markdown
1. Read 讀取目標檔案。
2. Think 決定修改範圍。
```

## Bad Example

- 步驟使用無序清單，且動詞沒有位於開頭。

```markdown
- 請先讀取目標檔案。
- 接著決定修改範圍。
```

# Rule 5 - 允許的步驟動詞

- 步驟動詞必須使用 `Read`、`Write`、`Think` 或 `Delegate`。
- `Read` 必須用於讀取檔案。
- `Write` 必須用於寫入檔案。
- `Think` 必須用於需要完成的推理或決策。
- `Delegate` 必須用於交給 script 或其他 Skill 執行的工作。
- 步驟不得使用未定義的動詞。

## Good Example

- 每個步驟都使用已定義且符合行為類型的動詞。

```markdown
1. Read 讀取規範檔案。
2. Think 決定需要修改的內容。
3. Write 修改目標檔案。
4. Delegate skill-form-rule。
```

## Bad Example

- 步驟使用未定義的 `Check` 動詞。

```markdown
1. Check 檢查目標檔案。
```

# Rule 6 - 步驟單一動作

- 每個步驟必須只包含一個動詞及一個對應行為。
- 需要不同動詞的行為必須拆分為不同步驟。
- 同一步驟不得同時要求讀取、推理、寫入或委派中的兩種以上行為。

## Good Example

- 讀取與寫入被拆分為兩個步驟。

```markdown
1. Read 依規範檢查目標檔案。
2. Write 修正不符合規範的內容。
```

## Bad Example

- 同一步驟同時要求檢查與修正。

```markdown
1. Read 檢查目標檔案並修正不符合規範的內容。
```
