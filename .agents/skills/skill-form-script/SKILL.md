---
name: skill-form-script
description: 規範並檢查 Skill 的 scripts/ 目錄下可由 AI 直接執行的 Python Script。建立、修改或檢查 Skill 使用的 Python Script 時必須使用此 Skill。
---

# SOP

## Phase 1: 定義 Script

1. Read [Python Script 介面與跨平台規範](rules/PythonScript介面與跨平台規範.md)並取得輸入、輸出、副作用及跨平台要求。
2. Think 依需求與已載入規範決定目標 Python Script 的執行介面、檔案操作及錯誤回報方式。

## Phase 2: 撰寫 Script

1. Read [Python Script 依賴規範](rules/PythonScript依賴規範.md)並取得 Python 版本、第三方套件及隔離執行要求。
2. Write 依需求與已載入規範建立或修改目標 Skill `scripts/` 目錄下的 Python Script 及必要的相鄰 lock file。

## Phase 3: 檢查 Script

1. Read [Python Script 驗證規範](rules/PythonScript驗證規範.md)並取得靜態檢查與受控執行要求。
2. Read 依已載入規範檢查目標 Python Script 及規範要求的相鄰 lock file 並列出不符合項目。
3. Delegate 目標 Python Script 使用受控測試資料驗證執行結果並列出失敗項目。

## Phase 4: 修正 Script

1. Write 依已載入規範修正目標 Python Script 及規範要求的相鄰 lock file 中的全部不符合與失敗項目。
