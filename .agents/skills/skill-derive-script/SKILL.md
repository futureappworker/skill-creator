---
name: skill-derive-script
description: 為已有 SOP 的 Skill 之指定步驟衍生可自動執行的 Python Script，並將該 Script 整合回原流程。當指定步驟適合透過 Python 自動化時必須使用此 Skill。
---

# SOP

## Phase 1: 定義衍生範圍

1. Read 讀取目標 Skill 的 `SKILL.md` 並取得使用者指定步驟、所屬 Phase 與相鄰步驟。
2. Read [Script 衍生適用性規範](rules/Script衍生適用性規範.md)並取得自動化適用條件與職責邊界要求。
3. Think 依已載入規範決定只交由 Python Script 執行的職責、輸入、輸出及副作用。
4. Read [Script 衍生整合規範](rules/Script衍生整合規範.md)並取得 Script 命名、路徑與 SOP 委派要求。
5. Think 依已載入規範決定目標 Python Script 的名稱、路徑、執行方式及指定步驟的整合方式。

## Phase 2: 建立衍生 Script

1. Delegate `skill-form-script` 依已決定的職責、介面、名稱及路徑建立目標 Python Script。

## Phase 3: 整合衍生 Script

1. Delegate `skill-form-sop` 修改目標 Skill 的 `SKILL.md`，將指定步驟改為依已載入規範執行目標 Python Script 的委派步驟。

## Phase 4: 檢查整合結果

1. Read 讀取修改後的目標 Skill `SKILL.md` 並檢查 Script 委派位置、執行方式、指定步驟行為目的及原流程完整性，列出全部不符合項目。
2. Read 讀取新增的目標 Python Script 及存在的相鄰 lock file，並檢查其職責、介面、依賴及副作用與指定步驟一致，列出全部不符合項目。

## Phase 5: 修正整合結果

1. Delegate `skill-form-script` 修正目標 Python Script 的全部不符合項目。
2. Delegate `skill-form-sop` 修正目標 Skill `SKILL.md` 中 SOP 的全部不符合項目。
