# Rule 1 - Template 成對與路徑命名

- 每份 Template 必須由不可分割的骨架檔案與範例檔案組成。
- 骨架檔案必須放在 `<skill-package>/templates/<樣版名稱>.<格式>`。
- 範例檔案必須放在 `<skill-package>/templates/<樣版名稱>.example.<格式>`。
- 骨架檔案與範例檔案必須位於同一個 `templates/` 目錄。
- 範例檔名中的 `example` 必須使用小寫。
- 建立、修改或移除任一檔案時，必須同步處理同一份 Template 的另一個檔案。
- 不得只建立骨架檔案或只建立範例檔案。

## Good Example

- 同一個 `api-request` Template 的骨架與範例位於相同目錄，並使用規定的成對命名。

```text
payment-skill/templates/api-request.json
payment-skill/templates/api-request.example.json
```

## Bad Example

- 同一個 `api-request` Template 只有骨架檔案，缺少不可分割的範例檔案。

```text
payment-skill/templates/api-request.json
```

# Rule 2 - 成對檔案副檔名一致

- 同一份 Template 的骨架檔案與範例檔案必須使用相同副檔名。
- 副檔名必須表示兩個檔案共同採用的內容格式。
- 不得以不同副檔名組成同一份 Template。

## Good Example

- 骨架與範例都使用 `.yaml` 副檔名，明確表示兩者採用相同格式。

```text
templates/deployment.yaml
templates/deployment.example.yaml
```

## Bad Example

- 骨架使用 `.yaml`，範例卻使用 `.json`，兩者無法形成格式一致的一組 Template。

```text
templates/deployment.yaml
templates/deployment.example.json
```

# Rule 3 - 骨架必須是可直接複製的完整結構

- 骨架檔案必須包含產出目標檔案所需的完整結構。
- 骨架中的固定內容、必要欄位與必要區段必須保留在可直接複製的位置。
- 使用者必須只需替換占位符即可得到結構完整的目標檔案。
- 骨架不得以省略號、僅列欄位名稱或局部片段代替必要結構。

## Good Example

- 骨架包含完整 JSON 物件、必要欄位與可替換值，複製後只需替換占位符。

```json
{
  "name": "{{SERVICE_NAME}}",
  "endpoint": "{{SERVICE_ENDPOINT}}",
  "retry": {
    "maxAttempts": "{{MAX_ATTEMPTS}}"
  }
}
```

## Bad Example

- 骨架只列出局部欄位並用省略號代替必要結構，無法直接複製成完整 JSON。

```json
{
  "name": "{{SERVICE_NAME}}",
  "...": "其他欄位"
}
```

# Rule 4 - 骨架占位符格式與辨識性

- 骨架中的可替換值必須使用 `{{UPPER_SNAKE_CASE}}` 格式。
- 占位符名稱必須以大寫英文字母開頭，並且只能包含大寫英文字母、數字與底線。
- 占位符名稱必須能辨識其代表的內容，不得使用無法判斷用途的通用名稱。
- 同一概念在骨架中重複出現時，必須使用相同占位符。

## Good Example

- 占位符使用大寫蛇形命名，且 `SERVICE_ENDPOINT` 能明確辨識待填內容。

```yaml
endpoint: "{{SERVICE_ENDPOINT}}"
```

## Bad Example

- 占位符未使用大寫蛇形命名，且 `value` 無法辨識待填內容。

```yaml
endpoint: "{{value}}"
```

# Rule 5 - 範例必須替換全部占位符

- 範例檔案必須將骨架中的每一個占位符替換為符合欄位語意的具體值。
- 範例檔案不得保留任何 `{{UPPER_SNAKE_CASE}}` 占位符。
- 範例值必須讓讀者能判斷替換後內容的格式與用途。

## Good Example

- 範例將骨架的服務名稱與端點占位符全部替換為具體值。

```yaml
name: "billing-api"
endpoint: "https://billing.example.com/v1"
```

## Bad Example

- 範例仍保留端點占位符，因此沒有完成全部替換。

```yaml
name: "billing-api"
endpoint: "{{SERVICE_ENDPOINT}}"
```

# Rule 6 - 骨架與範例結構逐項對應

- 範例檔案的欄位、區段、層級與排列必須逐項對應骨架檔案。
- 骨架中的每個固定內容與占位符位置，必須在範例的相同結構位置提供對應內容。
- 範例不得新增骨架中不存在的欄位或區段。
- 範例不得省略骨架中存在的欄位或區段。

## Good Example

- 範例與骨架具有相同欄位和巢狀層級，差異僅為占位符已替換成具體值。

```yaml
# templates/service.yaml
service:
  name: "{{SERVICE_NAME}}"
  port: "{{SERVICE_PORT}}"

# templates/service.example.yaml
service:
  name: "orders-api"
  port: "8080"
```

## Bad Example

- 範例省略骨架的 `port`，並新增骨架不存在的 `owner`，因此無法逐項對應。

```yaml
# templates/service.yaml
service:
  name: "{{SERVICE_NAME}}"
  port: "{{SERVICE_PORT}}"

# templates/service.example.yaml
service:
  name: "orders-api"
  owner: "platform-team"
```

# Rule 7 - Template 只包含目標檔案內容

- 骨架與範例必須只包含目標格式可接受且屬於目標檔案的內容。
- 操作說明、使用步驟與規範條列必須放在 Template 以外的文件。
- Template 不得混入描述如何複製、替換或檢查內容的操作說明。
- Template 不得混入用來約束 AI 如何使用該 Template 的條列規範。
- 當規範性內容本身屬於目標檔案格式時，可以將其作為骨架結構或占位內容保留。

## Good Example

- 骨架只包含可直接成為目標設定檔的 YAML 結構。

```yaml
service:
  name: "{{SERVICE_NAME}}"
  port: "{{SERVICE_PORT}}"
```

## Bad Example

- 骨架在目標 YAML 結構中混入如何複製及替換 Template 的操作說明。

```yaml
# 使用步驟：
# 1. 複製本檔案。
# 2. 必須替換全部占位符。
service:
  name: "{{SERVICE_NAME}}"
  port: "{{SERVICE_PORT}}"
```
