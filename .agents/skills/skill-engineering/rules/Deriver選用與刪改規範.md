# Rule 1 - 先建立基準 SOP 再選用 Deriver

- 選用 Deriver 前，目標 Skill 必須先具備符合目標或已確認根因方向的基準 SOP。
- 基準 SOP 必須能看出 Phase、步驟、輸入、輸出與委派邊界。
- 當指定步驟同時包含多個目的時，必須先使用 `skill-form-sop` 拆分步驟，再判斷 Deriver。
- 不得在主流程尚未穩定前預先建立 Rule File、Template 或 Script。

## Good Example

- 先把混合職責拆成可判斷的步驟，再分別選用 Deriver。

```text
原步驟：Write 撰寫報告並檢查格式與發布結果。
基準 SOP 調整：拆成生成報告、檢查格式、發布結果三個步驟後，再判斷生成報告是否適合 Template 或 Script。
```

## Bad Example

- 主流程仍混雜多個目的時就直接衍生模組，會造成職責不清。

```text
原步驟：Write 撰寫報告並檢查格式與發布結果。
衍生方式：直接建立一個處理全部工作的 Script。
```

# Rule 2 - Rule File 用於行為約束與品質判斷

- 指定步驟需要命名規則、品質標準、禁止事項、判斷條件或邊界案例時，必須優先考慮 `skill-derive-rule`。
- Rule File 必須只描述指定步驟需要的單一規則主題。
- Rule File 不得用來保存固定檔案骨架、完整範例成品或可自動執行的演算法。
- 當規則只服務於已刪除或已合併的步驟時，必須刪除或併入仍被使用的 Rule File。

## Good Example

- 指定步驟需要可檢查的品質標準，因此適合衍生 Rule File。

```text
指定步驟：Read 檢查根因確認提案並列出不符合項目。
選用：skill-derive-rule，建立根因確認提案內容完整性規範。
```

## Bad Example

- 固定檔案結構不應放在 Rule File 中。

```text
指定步驟：Write 生成固定章節的 Markdown 報告。
選用：skill-derive-rule，把完整報告骨架寫成規則條列。
```

# Rule 3 - Template 用於固定輸出結構

- 指定步驟會生成固定檔案內容結構時，必須考慮 `skill-derive-template`。
- 固定結構必須能由骨架檔案與完整範例檔案成對表達。
- Template 不得承載品質判斷、流程控制或行為約束。
- 當既有 Template 固化錯誤結構或不再被 SOP 使用時，必須替換或刪除整組骨架與範例。

## Good Example

- 輸出具有固定章節與欄位，因此適合衍生 Template。

```text
指定步驟：Write 產出根因確認提案檔案。
選用：skill-derive-template，建立提案骨架與完整範例。
```

## Bad Example

- 使用 Template 取代品質判斷，會讓樣板承擔錯誤職責。

```text
指定步驟：Think 判斷根因是否成立。
選用：skill-derive-template，建立一份寫著「根因必須正確」的樣板。
```

# Rule 4 - Script 用於確定性自動化

- 指定步驟包含可由相同輸入重複執行的確定性操作時，必須考慮 `skill-derive-script`。
- Script 職責必須有明確輸入、輸出、exit code 與副作用邊界。
- Script 不得接管需求解讀、使用者期待判斷、根因判定或設計取捨。
- 當既有 Script 接管了 AI 判斷或跨越指定步驟邊界時，必須縮小職責、重寫或刪除。

## Good Example

- 機械式掃描可重複執行，適合交由 Script。

```text
指定步驟：Read 掃描目標 Skill 目錄並列出未被 SKILL.md 載入或委派的檔案。
選用：skill-derive-script，建立孤兒模組掃描 Script。
```

## Bad Example

- 根因判斷需要語意理解與設計取捨，不應交給 Script。

```text
指定步驟：Think 判斷使用者不滿意的根因。
選用：skill-derive-script，讓 Script 自動決定哪個 Skill 設計錯誤。
```

# Rule 5 - 保留 SOP 用於不可形式化的判斷

- 當指定步驟主要是理解需求、設計取捨、根因判斷或與使用者確認時，必須保留於 SOP。
- 保留於 SOP 的步驟仍可搭配 Rule File 取得判斷標準。
- 不得因為可以寫成程式或樣板，就把不可形式化的判斷抽成 Script 或 Template。
- SOP 中的判斷步驟過大時，必須先拆分而不是直接衍生模組。

## Good Example

- AI 判斷保留在 SOP，規範只提供檢查標準。

```text
指定步驟：Think 判斷根因確認提案是否足以進入改寫。
選用：保留於 SOP，並使用 Rule File 提供確認提案要求。
```

## Bad Example

- 把設計取捨硬塞進 Script，會讓流程失去可解釋性。

```text
指定步驟：Think 選擇最適合的 Skill 邊界。
選用：skill-derive-script，自動輸出唯一正確的 Skill 邊界。
```

# Rule 6 - 模組刪改必須依 SOP 使用關係決定

- 每個 Rule File、Template 與 Script 必須能被目標 SOP 按需載入或委派。
- 未被 SOP 載入或委派的模組必須視為孤兒模組並列入刪除、合併或重新整合候選。
- 與已確認根因衝突的模組必須重寫或刪除，不得只靠新增規則繞過。
- 刪除模組前必須確認沒有其他仍保留的 Skill 或 SOP 步驟需要該模組。

## Good Example

- 刪改依據來自 SOP 使用關係與根因判斷。

```text
模組盤點：rules/舊輸出格式規範.md 未被 SKILL.md 載入，且描述的格式與已確認的新輸出期待衝突。
處置：刪除該 Rule File，並以新 SOP 使用的規範取代。
```

## Bad Example

- 只因為檔案存在就保留，會讓過時規則繼續干擾後續維護。

```text
模組盤點：rules/舊輸出格式規範.md 已經沒有任何 SOP 載入。
處置：保留檔案，避免改太多。
```

# Rule 7 - 編排計畫必須說明選用與不選用理由

- 執行 Deriver 前，必須產出模組化編排計畫。
- 編排計畫必須列出每個指定步驟、選用的 Deriver、保留於 SOP 的步驟、刪改的既有模組與理由。
- 對於未選用的 Deriver，必須說明不適用的原因。
- 編排計畫不得只列要新增的檔案，而忽略刪除、合併、保留或不選用理由。

## Good Example

- 計畫同時說明選用、保留、刪除與不選用理由。

```text
編排計畫：
- Phase 3 Step 3：保留於 SOP，因為根因判斷需要 AI 語意推理；不選用 Script。
- Phase 3 Step 4：使用 skill-derive-rule，因為需要根因確認提案的品質標準。
- rules/舊規範.md：刪除，因為未被 SOP 載入且與新流程衝突。
```

## Bad Example

- 計畫只列新增項目，無法判斷是否真的消除根因。

```text
編排計畫：
- 新增一份規則。
- 新增一個樣板。
```
