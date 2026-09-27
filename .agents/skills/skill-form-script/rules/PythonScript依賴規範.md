# Rule 1 - PEP 723 Metadata

- 每個目標 Python Script 都必須包含一個 PEP 723 `script` metadata block。
- Metadata block 必須包含 `requires-python` 與 `dependencies`。
- 沒有第三方套件時，`dependencies` 必須宣告為空陣列。
- 同一個 Script 不得包含兩個以上的 `script` metadata block。

## Good Example

- Script 明確宣告 Python 版本，並以空陣列表達沒有第三方依賴。

```python
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
```

## Bad Example

- Script 只有 Python 程式碼，執行者無法從檔案得知相容的 Python 版本與依賴。

```python
from pathlib import Path

print(Path.cwd())
```

# Rule 2 - 第三方依賴完整宣告

- Script 直接匯入的每個第三方套件都必須在 `dependencies` 中使用有效的 PEP 508 dependency specifier 宣告。
- Python 標準函式庫不得列入 `dependencies`。
- Dependency specifier 應該限制已驗證的相容版本範圍；未限制版本時，必須說明無法限制的具體理由。
- Script 不得依賴目標 Skill 外部專案的 `pyproject.toml`、`requirements.txt` 或已啟用環境才能執行。

## Good Example

- `requests` 是第三方套件且已限制相容範圍；`json` 屬於標準函式庫，因此沒有列入。

```python
# /// script
# requires-python = ">=3.11"
# dependencies = ["requests>=2.32,<3"]
# ///

import json
import requests
```

## Bad Example

- Script 匯入 `requests`，卻只假設呼叫端已經安裝套件。

```python
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

import requests
```

# Rule 3 - 隔離執行

- 具有 PEP 723 metadata 的 Script 必須使用 `uv run --script <script-path>` 執行。
- `uv` 必須依 metadata 建立或重用隔離環境，不得將 Script 依賴安裝至系統 Python。
- Script 不得在執行期間呼叫 `pip`、`uv pip` 或其他套件安裝命令。
- `uv` 不存在時，執行者必須依 [uv 官方安裝方式](https://docs.astral.sh/uv/getting-started/installation/)選擇目前平台支援的方式完成安裝後再執行。
- uv 安裝失敗時，執行者必須停止並回報原因。
- 執行者不得以全域 `pip install` 安裝 Script dependencies，或將其作為 uv 依賴解析失敗的替代方案。

## Good Example

- 執行命令會讀取 Script 自帶的 metadata，並在隔離環境中解析依賴。

```text
uv run --script scripts/generate-report.py --input data.json
```

## Bad Example

- 命令先污染目前 Python 環境，而且依賴版本沒有由 Script 自身決定。

```text
pip install requests
python scripts/generate-report.py --input data.json
```

# Rule 4 - Lock File 使用條件

- 一般的非破壞性 Script 應該只使用 PEP 723 metadata，不得預設建立 lock file。
- 當 Script 執行資料遷移、破壞性操作，或輸出必須由完整相依版本重現時，必須使用 `uv lock --script <script-path>` 產生相鄰的 `<script-name>.py.lock`。
- Lock file 必須與對應 Script 一起保存。
- 不符合前述條件卻建立 lock file 時，必須說明增加維護成本的具體理由。

## Good Example

- 資料庫遷移需要固定完整相依版本，因此 Script 與相鄰 lock file 成對保存。

```text
scripts/migrate-records.py
scripts/migrate-records.py.lock
```

## Bad Example

- 一次性的唯讀文字統計 Script 無條件建立專案層級 lock file，擴大了管理範圍。

```text
scripts/count-words.py
uv.lock
```

# Rule 5 - Python 版本相容範圍

- `requires-python` 必須包含 Script 實際使用語法及標準函式庫所需的最低 Python 版本。
- `requires-python` 不得宣告低於 Script 實際可執行的版本。
- Script 沒有已知上限時，可以只宣告最低版本。
- Script 使用具有已知不相容上限的功能時，必須同時宣告上限。

## Good Example

- Script 使用 Python 3.11 才提供的 `tomllib`，因此最低版本宣告為 3.11。

```python
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

import tomllib
```

## Bad Example

- Metadata 宣告支援 Python 3.9，但程式碼直接匯入 Python 3.11 才提供的 `tomllib`。

```python
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///

import tomllib
```
