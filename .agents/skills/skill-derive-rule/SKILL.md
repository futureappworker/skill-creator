---
name: skill-derive-rule
description: 為已有 SOP 的 Skill 之指定步驟衍生按需載入的 Rule File，並將該規則整合回原流程。當使用者要加強特定步驟的把關規則時必須使用此 Skill。
---

# SOP

## Phase 1: 定義衍生範圍

1. Read 讀取目標 Skill 的 `SKILL.md` 並取得使用者指定步驟、所屬 Phase 與相鄰步驟。
2. Think 決定只適用於指定步驟的規則範圍與明確要求。
3. Read [規則衍生設計規範](rules/規則衍生設計規範.md)並取得 Rule File 命名與 SOP 整合要求。
4. Think 依已載入規範決定新增 Rule File 的名稱、路徑、載入位置及使用方式。

## Phase 2: 建立衍生規則

1. Delegate `skill-form-rule` 依已決定的規則範圍與要求建立目標 Rule File。

## Phase 3: 整合衍生規則

1. Delegate `skill-form-sop` 修改目標 Skill 的 `SKILL.md`，在指定步驟首次需要規則時按需載入目標 Rule File，並使指定步驟使用已載入規範。

## Phase 4: 檢查整合結果

1. Read 讀取修改後的目標 Skill `SKILL.md` 並檢查 Rule File 載入位置、指定步驟使用方式及原流程完整性，列出全部不符合項目。
2. Read 讀取新增的目標 Rule File 並檢查其規則範圍與指定步驟一致，列出全部不符合項目。

## Phase 5: 修正整合結果

1. Delegate `skill-form-rule` 修正目標 Rule File 的全部不符合項目。
2. Delegate `skill-form-sop` 修正目標 Skill `SKILL.md` 中 SOP 的全部不符合項目。
