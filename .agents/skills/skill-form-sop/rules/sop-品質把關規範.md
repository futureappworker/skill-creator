# Rule 1 - Read 行為完整性

- `Read` 步驟必須指出要讀取的檔案或明確可識別的檔案類型。
- 需要從讀取結果取得特定資訊時，`Read` 步驟必須指出要取得或檢查的內容。
- `Read` 步驟不得只寫「讀取相關資料」等無法識別來源的描述。

## Good Example

- 步驟指出規範檔案及需要檢查的內容。

```markdown
1. Read [SOP 格式規範](rules/sop-格式規範.md)並檢查允許的步驟動詞。
```

## Bad Example

- 步驟沒有指出讀取來源及需要取得的內容。

```markdown
1. Read 讀取相關資料。
```

# Rule 2 - Write 行為完整性

- `Write` 步驟必須指出要寫入或修改的目標檔案。
- `Write` 步驟必須指出要產出的內容或修改目的。
- `Write` 步驟不得省略寫入目標。

## Good Example

- 步驟同時指出目標檔案及要寫入的內容。

```markdown
1. Write 將符合格式規範的 SOP 寫入目標 Skill 的 `SKILL.md`。
```

## Bad Example

- 步驟只要求撰寫內容，沒有指出寫入目標。

```markdown
1. Write 撰寫一份符合規範的 SOP。
```

# Rule 3 - Think 行為完整性

- `Think` 步驟必須指出需要完成的決策或推理結果。
- `Think` 步驟必須提供後續步驟可以使用的明確結果。
- `Think` 步驟不得只寫「思考」或「分析」而未指定結果。

## Good Example

- 步驟指出要決定的 Phase 順序及拆分方式。

```markdown
1. Think 決定 SOP 的 Phase 順序及每個 Phase 的單一目的。
```

## Bad Example

- 步驟沒有指出思考後必須得到的結果。

```markdown
1. Think 分析 SOP。
```

# Rule 4 - Delegate 行為完整性

- `Delegate` 步驟必須指定接手工作的 script 或其他 Skill。
- `Delegate` 步驟必須指出要交付的工作。
- `Delegate` 步驟不得重寫被委派對象內部的執行流程。

## Good Example

- 步驟指定 Skill 及交付工作，沒有重寫該 Skill 的內部流程。

```markdown
1. Delegate `skill-form-rule` 撰寫 SOP 的 Rule File。
```

## Bad Example

- 步驟未指定委派對象，並直接展開內部做法。

```markdown
1. Delegate 先編號每條 Rule，再加入 Good Example 與 Bad Example，最後檢查格式。
```

# Rule 5 - 步驟可驗證性

- 每個步驟必須描述可以判斷是否完成的具體行為。
- 步驟中的目標、輸入或結果必須至少有一項可以明確識別。
- 步驟不得使用「適當處理」、「視情況調整」或「完成相關工作」等無法驗證的描述。

## Good Example

- 步驟以「列出不符合項目」提供可驗證的結果。

```markdown
1. Read 依兩份規範檢查目標 SOP 並列出不符合項目。
```

## Bad Example

- 步驟使用無法判斷完成條件的模糊描述。

```markdown
1. Read 適當檢查目標 SOP。
```

# Rule 6 - 檢查與修正閉環

- 產出或修改檔案的 SOP 必須在寫入後安排檢查步驟。
- 檢查步驟之後必須安排修正不符合項目的步驟。
- 檢查與修正必須分屬目的不同的 Phase。
- 沒有寫入行為的唯讀 SOP 可以省略修正 Phase。

## Good Example

- 寫入後依序安排獨立的檢查與修正 Phase。

```markdown
## Phase 2: 撰寫 SOP

1. Write 將 SOP 寫入目標 Skill 的 `SKILL.md`。

## Phase 3: 檢查 SOP

1. Read 依規範檢查目標 SOP 並列出不符合項目。

## Phase 4: 修正 SOP

1. Write 修正目標 Skill 的 `SKILL.md` 中全部不符合項目。
```

## Bad Example

- 寫入後只有檢查 Phase，缺少修正不符合項目的 Phase。

```markdown
## Phase 2: 撰寫 SOP

1. Write 將 SOP 寫入目標 Skill 的 `SKILL.md`。

## Phase 3: 檢查 SOP

1. Read 依規範檢查目標 SOP 並列出不符合項目。
```

## Exceptions

- 當 SOP 全程只有讀取、推理或委派行為且不會寫入任何檔案時，可以省略修正 Phase。
