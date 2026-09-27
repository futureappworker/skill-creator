# Rule 1 - Script 名稱與路徑

- Script 名稱必須描述指定步驟委派的單一自動化職責。
- Script 檔名必須使用小寫英文字母、數字與連字號，並以 `.py` 結尾。
- Script 必須放在目標 Skill 的 `scripts/` 目錄。
- Script 路徑必須使用相對於目標 Skill `SKILL.md` 的 `scripts/<script-name>.py` 形式。
- Script 路徑不得覆寫與本次職責不同的既有檔案。

## Good Example

- 名稱描述報告生成職責，路徑位於目標 Skill 的 `scripts/` 目錄。

```text
scripts/generate-report.py
```

## Bad Example

- 名稱無法識別職責、使用大寫與底線，且沒有放在 `scripts/` 目錄。

```text
helpers/Do_Stuff.py
```

# Rule 2 - 指定步驟改為委派

- 指定步驟必須改用 `Delegate` 動詞。
- 委派步驟必須以 Markdown link 明確指向本次建立的 Script 相對路徑。
- 委派步驟必須保留原指定步驟的行為目的。
- 委派步驟必須指出要交付給 Script 的工作，不得在 SOP 重寫 Script 的內部演算法。
- 原指定步驟已經使用 `Delegate` 時，必須更新委派對象與工作，不得新增重複步驟。

## Good Example

- 原本的報告生成目的被保留，並明確委派給目標 Script。

```markdown
3. Delegate [報告生成 Script](scripts/generate-report.py) 依掃描結果生成目標 Markdown 報告檔案。
```

## Bad Example

- 步驟仍使用 `Write`，也沒有指出實際執行的 Script。

```markdown
3. Write 使用 Python 自動生成報告。
```

# Rule 3 - 執行方式與參數

- 委派步驟必須要求使用 `uv run --script` 執行目標 Script。
- 委派步驟必須指出 Script 所需輸入與預期輸出；具體值由前序步驟產生時，可以引用該結果。
- 委派步驟不得要求先啟用 virtual environment 或手動安裝 Script dependencies。
- `uv` 不可用時，執行者必須依 [uv 官方安裝方式](https://docs.astral.sh/uv/getting-started/installation/)選擇目前平台支援的方式安裝；安裝失敗時必須停止並回報原因。

## Good Example

- 執行器、Script、輸入與輸出都能從委派步驟識別。

```markdown
3. Delegate 使用 `uv run --script` 執行 [報告生成 Script](scripts/generate-report.py)，讀取已產生的掃描結果並寫入目標報告路徑。
```

## Bad Example

- 步驟沒有指定隔離執行方式、輸入或輸出。

```markdown
3. Delegate 執行報告 Script。
```

# Rule 4 - 原流程完整性

- 指定步驟所屬 Phase 必須保留原有目的及位置。
- 未被指定的步驟必須保留原有內容與相對順序。
- 指定步驟改為委派後，所屬 Phase 的步驟必須依執行順序重新連續編號。
- 不得修改與本次 Script 整合無關的 Phase、Rule File 載入或 Template 載入。
- Script 產出必須繼續供原本依賴指定步驟結果的後續步驟使用。

## Good Example

- 只有指定步驟改成 Script 委派，前後步驟與 Phase 目的維持不變。

```markdown
## Phase 2: 生成報告

1. Read 讀取掃描結果並取得問題清單。
2. Delegate 使用 `uv run --script` 執行 [報告生成 Script](scripts/generate-report.py)，依問題清單生成目標報告檔案。
3. Read 檢查目標報告檔案並列出不符合項目。
```

## Bad Example

- 整合 Script 時刪除了原本的檢查步驟，破壞既有流程閉環。

```markdown
## Phase 2: 生成報告

1. Delegate 使用 `uv run --script` 執行 [報告生成 Script](scripts/generate-report.py)，生成並自行核准目標報告。
```

# Rule 5 - Script 與 SOP 契約一致

- SOP 委派步驟提及的每個必要輸入都必須能對應至 Script 的命令列介面。
- SOP 委派步驟承諾的每個輸出都必須由 Script 實際產生。
- SOP 與 Script 對相對路徑、標準輸入、標準輸出及 exit code 的解釋必須一致。
- Script 增加必要參數或改變輸出位置時，必須同步修改委派步驟。

## Good Example

- SOP 所述輸入與輸出都能對應到 Script 的參數。

```markdown
Delegate 使用 `uv run --script` 執行 [正規化 Script](scripts/normalize-data.py)，以來源 JSON 作為 `--input` 並以目標 JSON 作為 `--output`。
```

## Bad Example

- SOP 要求輸出檔，但 Script 只輸出到標準輸出且沒有 `--output` 參數。

```markdown
Delegate 執行 [正規化 Script](scripts/normalize-data.py) 並將結果寫入目標 JSON 檔。
```
