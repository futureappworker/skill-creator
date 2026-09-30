---
name: skill-engineering
description: 編排模組化方式建立或根本性優化 Cursor Agent Skill。Use when creating a new Skill, refactoring an existing Skill, diagnosing unsatisfactory Skill output, or coordinating skill-form-sop, skill-derive-rule, skill-derive-template, and skill-derive-script to keep Skill SOP, rules, templates, and scripts maintainable.
---


# SOP

## Phase 1: 判斷工程模式

1. Read 讀取使用者需求、目標 Skill 檔案及相關 Skill 清單，取得本次建立或優化範圍。
2. Think 決定本次任務是建立新 Skill、優化既有 Skill，或同時包含兩種工程模式。

## Phase 2: 建立新 Skill 目標

1. Think 當任務包含建立新 Skill 時，決定目標 Skill 的用途、觸發條件、主要成果與必要工程邊界。
2. Delegate 當任務包含建立新 Skill 時，交給 `skill-form-sop` 依已決定的目標建立目標 Skill 的最小可執行 SOP。

## Phase 3: 分析優化根因

1. Read 當任務包含優化既有 Skill 時，讀取 [優化根因分析規範](rules/優化根因分析規範.md)並取得期待釐清、落差回推與確認閘門要求。
2. Read 當任務包含優化既有 Skill 時，讀取使用者描述、相關對話脈絡、目標 Skill、上下游委派 Skill 及既有輸出結果。
3. Think 當任務包含優化既有 Skill 時，依已載入規範推導使用者期待、現況落差、執行路徑、根因位置與非根因排除項目。
4. Think 當任務包含優化既有 Skill 時，依已載入規範產出根因確認提案，並在使用者確認前停止後續改寫。

## Phase 4: 重整基準 SOP

1. Delegate `skill-form-sop` 依新建目標或已確認的根因改造方向，建立或重整目標 Skill 的 `SKILL.md`。

## Phase 5: 診斷模組化與刪改機會

1. Read [Deriver 選用與刪改規範](rules/Deriver選用與刪改規範.md)並取得 Rule File、Template、Script、SOP 拆分與模組刪改的判斷要求。
2. Read 讀取目標 Skill 的 `SKILL.md`、`rules/`、`templates/`、`scripts/` 及相關上下游 Skill，取得每個 Phase、步驟、模組與委派關係。
3. Think 依已載入規範決定每個步驟應保留於 SOP、衍生 Rule File、衍生 Template、衍生 Script、先拆分 SOP、或刪改既有模組。
4. Think 產出模組化編排計畫，列出每個指定步驟、選用 Deriver、刪改項目及理由。

## Phase 6: 執行模組化工程

1. Delegate `skill-derive-rule` 依模組化編排計畫為需要規則把關的指定步驟衍生或重整 Rule File。
2. Delegate `skill-derive-template` 依模組化編排計畫為需要固定輸出結構的指定步驟衍生或替換 Template。
3. Delegate `skill-derive-script` 依模組化編排計畫為可確定性自動化的指定步驟衍生或重整 Python Script。
4. Write 依模組化編排計畫刪除目標 Skill 中已確認不再被 SOP 按需載入、委派或造成根因的過時模組檔案。

## Phase 7: 檢查整體工程結果

1. Delegate `skill-form-sop` 檢查並修正目標 Skill 的 `SKILL.md`。
2. Read 依已載入規範檢查目標 Skill 的 `rules/`、`templates/`、`scripts/` 是否都被 SOP 按需載入或委派，並列出孤兒模組、重複職責與殘留根因。
3. Think 判斷整體 Skill 是否已消除根因或符合新建目標，並維持 SOP 精簡、模組職責單一與按需載入。
