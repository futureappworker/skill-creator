---
name: plan-with-class-diagram
description: 在撰寫程式前先以 Mermaid 類別圖提案類別組織，取得使用者確認後再依圖依序開發。Use when starting non-trivial implementation, designing class structure, refactoring modules, or when the user invokes plan-with-class-diagram.
---

# SOP

## Phase 1: 理解需求

1. Read 使用者請求與任務相關既有程式碼，取得開發範圍與約束。
2. Think 列出預期新增的類別、介面、模組及其職責。

## Phase 2: 提案類別圖

1. Read [類別圖格式規範](rules/class-diagram-規範.md)並取得格式與繪製要求。
2. Read [類別關係判定規範](rules/類別關係判定規範.md)並取得關係類型與依賴方向的判定要求。
3. Think 依已載入規範決定類別間繼承、實作、組合、聚合與依賴關係。
4. Think 決定本次計劃的兩位數編號、名稱、Mermaid classDiagram、類別職責與關係說明，以及回覆中的使用者確認問題。
5. Read [類別設計提案骨架](templates/類別設計提案.md)並取得固定內容結構。
6. Read [類別設計提案範例](templates/類別設計提案.example.md)並取得完整使用方式。
7. Write 依已載入樣板與範例及已載入規範，將 Mermaid classDiagram、類別職責及關係說明寫入專案根目錄的 `specs/plan/<NN>-<本次計劃名稱>/class-diagram-proposal.md`。

## Phase 3: 等待確認

1. Think 依使用者回覆判斷：確認則進入 Phase 4，要求修改則回到 Phase 2，未確認則停止且不撰寫程式碼。

## Phase 4: 按圖施工

1. Read 依已載入規範取得實作順序要求。
2. Think 依類別圖相依性排出實作順序。
3. Write 依已載入規範、實作順序與已確認類別圖，依序實作目標程式碼檔案中的類別、方法與關係。

## Phase 5: 檢查實作

1. Read 依已載入規範與已確認類別圖檢查目標程式碼檔案並列出不符合項目。

## Phase 6: 修正實作

1. Write 修正目標程式碼檔案中全部不符合項目。
