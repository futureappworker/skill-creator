# Rule 1 - 可自動化職責

- 只有當指定步驟包含可由相同輸入重複執行的確定性操作時，才可以衍生 Python Script。
- 適合衍生的操作可以包含檔案轉換、結構化資料處理、機械式驗證或固定命令編排。
- 指定步驟沒有可分離的確定性操作時，不得衍生 Script。
- 是否衍生 Script 必須依指定步驟的行為判斷，不得只因操作可以用 Python 撰寫就衍生。

## Good Example

- 指定步驟將固定格式 JSON 轉成報告，輸入、轉換與輸出都可重複驗證。

```text
指定步驟：Write 將掃描結果 JSON 轉換成 Markdown 報告。
衍生範圍：由 Python Script 執行 JSON 解析、排序及 Markdown 生成。
```

## Bad Example

- 指定步驟需要判斷需求與設計方案，沒有確定性演算法可以取代推理。

```text
指定步驟：Think 決定最適合使用者需求的系統架構。
衍生範圍：由 Python Script 自動選擇最佳架構。
```

# Rule 2 - 保留 AI 判斷

- Script 職責不得包含需求解讀、品質取捨、設計決策或無法形式化的語意判斷。
- 指定步驟同時包含判斷與機械操作時，必須只將機械操作交給 Script。
- AI 必須在委派前完成 Script 所需的判斷，或在委派後解讀 Script 的結構化結果。
- 不得以 Script 取代原流程要求的人類確認。

## Good Example

- AI 決定保留哪些欄位，Script 只依明確欄位清單進行轉換。

```text
AI 職責：決定報告需要保留的欄位。
Script 職責：依 --fields 參數擷取欄位並生成報告。
```

## Bad Example

- Script 被要求自行判斷哪些內容「重要」，但沒有可驗證標準。

```text
Script 職責：閱讀所有資料並挑選最重要的內容。
```

# Rule 3 - 可識別執行契約

- 衍生範圍必須能指出 Script 的輸入來源、輸出結果與副作用。
- 輸入或輸出無法從指定步驟識別時，必須先由 AI 決定執行契約，再建立 Script。
- Script 的成功條件必須能透過 exit code、輸出檔或標準輸出驗證。
- 無法定義成功條件時，不得衍生 Script。

## Good Example

- 輸入、輸出及成功條件都有明確識別方式。

```text
輸入：--input 指定的 JSON 檔。
輸出：--output 指定的 Markdown 檔。
成功條件：exit code 0 且輸出檔通過標題與章節檢查。
```

## Bad Example

- 沒有定義輸入、輸出或可驗證結果。

```text
輸入：相關資料。
輸出：處理完成。
成功條件：結果看起來正確。
```

# Rule 4 - 單一步驟職責邊界

- 每次衍生必須只服務使用者指定的一個 SOP 步驟。
- Script 可以包含完成該步驟所需的內部子操作。
- Script 不得接管相鄰步驟或其他 Phase 的職責。
- 指定步驟範圍過大且包含多個獨立目的時，必須先使用 `skill-form-sop` 拆分步驟，再衍生 Script。

## Good Example

- Script 只處理指定的報告生成步驟，後續品質審查仍由原 SOP 執行。

```text
指定步驟：Write 生成報告檔案。
Script 職責：生成報告檔案。
保留步驟：Read 檢查報告內容品質。
```

## Bad Example

- Script 同時接管生成、審查與發布三個不同目的。

```text
指定步驟：Write 生成報告檔案。
Script 職責：生成報告、判斷內容品質並發布到正式網站。
```
