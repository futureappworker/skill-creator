# Rule 1 - 靜態一致性檢查

- 執行測試前必須檢查 Script 的第三方 import 是否全部存在於 PEP 723 `dependencies`。
- 執行測試前必須檢查 `requires-python` 是否涵蓋 Script 使用的語法與標準函式庫。
- 執行測試前必須檢查命令列必要參數、輸出位置及副作用是否能從介面識別。
- 發現靜態不一致時，必須列為不符合項目。

## Good Example

- 檢查同時涵蓋 import、Python 版本與執行介面。

```text
檢查結果：
- requests 已宣告於 dependencies。
- tomllib 所需最低版本與 requires-python 一致。
- --input 與 --output 均為必要參數。
```

## Bad Example

- 只確認檔案副檔名，沒有檢查依賴或介面。

```text
檢查結果：檔案名稱以 .py 結尾，因此符合規範。
```

# Rule 2 - 隔離測試命令

- 目標 Script 必須使用 `uv run --script <script-path>` 執行測試。
- 測試不得依賴已啟用的 virtual environment 或目前專案的套件。
- Script 定義 `--help` 時，必須先驗證 `--help` 能成功顯示介面。
- uv 無法解析 Python 或依賴時，必須將完整錯誤列為失敗項目，不得改用系統 Python 略過。

## Good Example

- 測試使用 Script 自身 metadata 建立隔離環境。

```text
uv run --script scripts/generate-report.py --help
```

## Bad Example

- 測試直接使用目前環境的 Python，因此無法驗證 PEP 723 metadata 是否完整。

```text
python scripts/generate-report.py --help
```

# Rule 3 - 成功與失敗案例

- 驗證必須至少包含一個代表性的成功案例。
- 驗證必須至少包含一個無效輸入或缺少必要輸入的失敗案例。
- 成功案例必須檢查 exit code 與預期輸出。
- 失敗案例必須檢查非零 exit code、錯誤訊息及沒有非預期副作用。
- 只有 `--help` 成功不得視為 Script 功能驗證完成。

## Good Example

- 同時驗證有效輸入的成品與無效輸入的失敗契約。

```text
成功案例：有效 JSON 輸入，exit code 0，輸出報告內容符合預期。
失敗案例：不存在的輸入檔，exit code 2，stderr 指出檔案路徑，沒有建立輸出檔。
```

## Bad Example

- 只顯示說明文字，沒有執行 Script 的實際職責。

```text
uv run --script scripts/generate-report.py --help
結果：成功，因此全部功能通過。
```

# Rule 4 - 受控測試資料

- 測試輸入與輸出必須使用可安全刪除的暫存目錄或專用 fixture。
- 測試不得修改使用者真實資料、正式服務或未提交的專案成果。
- 具有外部服務副作用的 Script 必須使用 dry-run、測試環境或替代介面驗證。
- 無法隔離副作用時，不得實際執行破壞性案例，且必須列出未驗證項目與原因。

## Good Example

- 測試將輸入與輸出限制在本次建立的暫存目錄。

```text
uv run --script scripts/normalize.py \
  --input /tmp/skill-script-test/input.json \
  --output /tmp/skill-script-test/output.json
```

## Bad Example

- 測試直接覆寫專案正式資料，失敗時無法安全復原。

```text
uv run --script scripts/normalize.py \
  --input data/production.json \
  --output data/production.json
```
