# Skill Creator

一套用來建立與維護 Cursor Agent Skill 的 skills。每個 Skill 以 SOP 為主流程，把格式與把關要求拆到 `rules/`，把固定輸出拆成 `templates/` 裡的骨架與範例，需要時才載入。

## Skills

### skill-form-sop

撰寫或修改 `SKILL.md` 裡的 SOP。檢查流程是否分階段、步驟是否可執行，以及內容是否精簡、規則與樣板是否按需載入。撰寫、審查或修正 SOP 時使用。

### skill-form-rule

撰寫或修改 Skill 的 `rules/` 底下的 Rule File。負責規則檔的結構與內容把關。建立、修改或檢查規則檔時使用。

### skill-form-template

撰寫或修改 Skill 的 `templates/` 底下的 Template。一份 Template 由骨架與範例兩個檔案組成：骨架定義固定內容結構，範例示範完整用法。建立、修改或檢查 Template 時使用。

### skill-form-script

撰寫或修改 Skill 的 `scripts/` 底下可由 AI 直接執行的 Python Script。以 PEP 723 宣告 Python 與第三方依賴，使用 uv 隔離執行，並檢查命令列介面、跨平台路徑、副作用與受控測試。建立、修改或檢查 Python Script 時使用。

### skill-derive-rule

為已有 SOP 的某個步驟補上按需載入的 Rule File，並把載入方式寫回原流程。先決定規則範圍，再交給 `skill-form-rule` 建立規則檔、交給 `skill-form-sop` 改 SOP。要加強特定步驟的把關規則時使用。

### skill-derive-template

為已有 SOP 裡會產出固定格式檔案的步驟，補上一份由骨架與範例組成的 Template，並把載入方式寫回原流程。先決定輸出結構，再交給 `skill-form-template` 建立樣板、交給 `skill-form-sop` 改 SOP。固定輸出適合用樣板表達時使用。

### skill-derive-script

為已有 SOP 裡可確定性自動化的指定步驟建立 Python Script，並將原步驟改為使用 uv 執行 Script 的委派。先界定 AI 判斷與 Script 職責，再交給 `skill-form-script` 建立腳本、交給 `skill-form-sop` 改 SOP。指定步驟適合以 Python 加速時使用。

### plan-with-class-diagram

開始寫程式前，先用 Mermaid 類別圖提案類別、職責與關係，寫入 `specs/plan/<編號>-<計劃名稱>/class-diagram-proposal.md`。使用者確認後才依圖的相依順序實作，最後對照類別圖檢查並修正。非小型實作、設計類別結構或重構模組時使用。

## 目錄

```
.agents/skills/
├── skill-form-sop/            # SOP 撰寫與檢查
├── skill-form-rule/           # Rule File 撰寫與檢查
├── skill-form-template/       # Template 撰寫與檢查
├── skill-form-script/         # Python Script 撰寫與檢查
├── skill-derive-rule/         # 從指定步驟衍生 Rule File
├── skill-derive-template/     # 從指定步驟衍生 Template
├── skill-derive-script/       # 從指定步驟衍生 Python Script
└── plan-with-class-diagram/   # 類別圖提案後再實作
```
