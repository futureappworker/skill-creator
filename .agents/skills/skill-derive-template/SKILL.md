---
name: skill-derive-template
description: 為已有 SOP 的 Skill 之指定檔案生成步驟衍生由骨架與範例組成的 Template，並將兩個檔案按需整合回原流程。當固定輸出格式適合以樣板表達時必須使用此 Skill。
---

# SOP

## Phase 1: 定義衍生範圍

1. Read 讀取目標 Skill 的 `SKILL.md` 並取得使用者指定步驟、所屬 Phase 與相鄰步驟。
2. Think 決定指定步驟生成檔案的固定內容結構範圍。
3. Read [樣板衍生設計規範](rules/樣板衍生設計規範.md)並取得 Template 命名與 SOP 整合要求。
4. Think 依已載入規範決定 Template 名稱、骨架與範例的兩條路徑、載入位置及使用方式。

## Phase 2: 建立 Template

1. Delegate `skill-form-template` 依已決定的固定輸出結構、名稱及格式建立目標骨架與範例檔案。

## Phase 3: 整合 Template

1. Delegate `skill-form-sop` 修改目標 Skill 的 `SKILL.md`，在指定步驟首次需要 Template 時按需載入骨架與範例檔案，並使指定步驟使用「已載入樣板與範例」。

## Phase 4: 檢查整合結果

1. Read 讀取修改後的目標 Skill `SKILL.md` 並檢查骨架與範例檔案的載入位置、指定步驟使用方式及原流程完整性，列出全部不符合項目。
2. Read 讀取新增的骨架與範例檔案並檢查其固定輸出結構與指定步驟一致，列出全部不符合項目。

## Phase 5: 修正整合結果

1. Delegate `skill-form-template` 修正目標骨架與範例檔案中的全部不符合項目。
2. Delegate `skill-form-sop` 修正目標 Skill `SKILL.md` 中 SOP 的全部不符合項目。
