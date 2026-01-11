# フォーマット変換 (Format Converter)

このディレクトリには、CSV、JSON、Excelなど、さまざまなデータ形式を相互に変換するためのツールを格納します。

## ツール一覧

### 1. CSV to JSON Converter (`csv_to_json.py`)

CSVファイルをJSONファイルに変換します。

#### 使い方

```bash
python3 csv_to_json.py [入力CSV] [出力JSON] [オプション]
```

#### オプション

- `input`: (必須) 変換元のCSVファイルパス。
- `output`: (必須) 変換先のJSONファイルパス。
- `--orientation`: (任意) JSONの出力形式 (`records`, `split`など)。デフォルトは `records`。
- `--indent`: (任意) JSONのインデント数。デフォルトは `4`。

---

### 2. JSON to CSV Converter (`json_to_csv.py`)

JSONファイルをCSVファイルに変換します。

#### 使い方

```bash
python3 json_to_csv.py [入力JSON] [出力CSV] [オプション]
```

#### オプション

- `input`: (必須) 変換元のJSONファイルパス。
- `output`: (必須) 変換先のCSVファイルパス。
- `--orientation`: (任意) JSONの入力形式 (`records`, `split`など)。デフォルトは `records`。

---
今後、ExcelとCSV/JSONの相互変換ツールなどを追加していく予定です。