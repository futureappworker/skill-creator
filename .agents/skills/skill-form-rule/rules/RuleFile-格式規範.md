# Rule 1 - Rule 標題與編號

- 每條 Rule 必須使用 `# Rule N - <Rule name>` 作為標題。
- `Rule` 與編號之間必須有一個空格。
- 同一個 Rule File 可以包含多條 Rule。
- 編號必須從 1 開始，並依出現順序連續遞增。

## Good Example

- 標題格式正確，且編號從 1 開始連續遞增。

```markdown
# Rule 1 - 命名格式

# Rule 2 - 必要欄位
```

## Bad Example

- `Rule1` 缺少空格，且下一條 Rule 跳過編號 2。

```markdown
# Rule1 - 命名格式

# Rule 3 - 必要欄位
```

# Rule 2 - 規範性措辭與約束強度

- Rule 標題下方必須使用條列內容描述規則。
- Rule 必須使用下列規範性措辭表達約束強度：
  - `必須`：強制遵守；除非 Rule 明確列出 Exceptions，否則不得偏離。
  - `不得`：強制禁止；除非 Rule 明確列出 Exceptions，否則不得執行。
  - `應該`：預設遵守；有具體理由時可以偏離，但必須說明理由。
  - `可以`：選擇性行為；採用或不採用都不影響合規性。
- 同一項要求必須只使用一種約束強度。
- 說明可以使用 Markdown 表格或 Code Section 補充格式定義。
- 不得使用 `最好`、`盡量`、`適當`、`合理` 或 `視情況` 等無法明確判斷強度的措辭。

## Good Example

- 每項要求都有明確的約束強度；其中 `應該`允許有具體理由的偏離。

```markdown
- 檔名必須使用小寫英文字母與連字號。
- 檔名不得包含空格。
- Rule 應該提供邊界情境的 Example；無法建立合理邊界情境時，可以省略，但必須說明理由。
- Rule 可以包含補充說明。
```

## Bad Example

- `盡量`、`適當`與`最好`無法判斷要求是否強制，也沒有定義偏離條件。

```markdown
- 檔名盡量使用小寫英文字母。
- 使用適當的分隔符號。
- 最好提供 Example。
```

# Rule 3 - Good Example 與 Bad Example

- 每條 Rule 都必須包含 `## Good Example` 與 `## Bad Example`。
- `Good Example` 必須說明案例遵守規則的原因。
- `Bad Example` 必須說明案例違反規則的原因。
- 原因說明必須只強調與該 Rule 有關的重點。

## Good Example

- 同時提供 Good Example、Bad Example 及各自的原因說明。

```markdown
## Good Example

- 名稱只包含允許的字元。

## Bad Example

- 名稱包含規則禁止的空格。
```

## Bad Example

- 缺少 Bad Example，也沒有解釋案例合規的原因。

```markdown
## Good Example

`user-profile`
```

# Rule 4 - Example 必須使用 Code Section

- `Good Example` 與 `Bad Example` 的實際案例必須放在 Code Section 中。
- Code Section 必須標記內容使用的語言，例如 `markdown`、`typescript` 或 `json`。
- Code Section 外只能放置案例的原因說明，不得直接放置實際案例。

## Good Example

- 實際案例由有語言標記的 Code Section 包住，原因說明則留在外部。

````markdown
- 欄位名稱符合 camelCase。

```typescript
const userName = "Ben";
```
````

## Bad Example

- 實際案例沒有使用 Code Section，也沒有標記語言。

```markdown
- 欄位名稱符合 camelCase。

const userName = "Ben";
```

# Rule 5 - Good Example 與 Bad Example 必須成對

- 同一條 Rule 的 Good Example 與 Bad Example 必須描述相同情境。
- 兩個 Example 必須只呈現合規與違規之間的必要差異。
- 不得使用彼此無關的資料或情境作為一組 Example。

## Good Example

- 兩個案例都在描述 TypeScript 變數命名，差異只有是否符合 camelCase。

```typescript
const userName = "Ben";
```

## Bad Example

- 同一情境使用 snake_case，清楚呈現違反 camelCase 規則的差異。

```typescript
const user_name = "Ben";
```

# Rule 6 - 例外與補充章節

- Rule 可以在 `Bad Example` 之後加入其他補充章節。
- 規則存在例外時，可以使用 `## Exceptions` 列出例外。
- 每項例外必須描述具體的觸發條件。
- 額外章節不得取代 `Good Example` 或 `Bad Example`。
- 下一條 Rule 必須從下一個 `# Rule N - <Rule name>` 開始。

## Good Example

- Exceptions 列出可直接判斷的觸發條件，且保留必要的 Example 章節。

```markdown
## Exceptions

- 當外部 API 的既有欄位使用 snake_case 時，可以保留原始欄位名稱。
```

## Bad Example

- `特殊情況` 沒有定義觸發條件，無法判斷何時能套用例外。

```markdown
## Exceptions

- 特殊情況可以不遵守此規則。
```

