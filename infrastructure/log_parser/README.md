# ログパーサー (Log Parser)

このディレクトリには、Webサーバーやアプリケーションのログファイルを解析するためのツールを格納します。

## ツール一覧

### 1. Apacheアクセスログ解析ツール (`access_log_parser.py`)

Apacheの共通ログ形式（Common Log Format）のアクセスログを解析し、情報を集計・フィルタリングします。

#### 使い方

コマンドラインで以下のコマンドを実行します。

```bash
python3 access_log_parser.py [ログファイル] [オプション]
```

#### コマンド例

- **IPアドレスごとのアクセス回数を集計**
  ```bash
  python3 access_log_parser.py access.log
  ```

- **特定のIPアドレスのアクセス記録を抽出**
  ```bash
  python3 access_log_parser.py access.log --ip 192.168.1.1
  ```

- **特定のステータスコード（例: 404）のログを集計**
  ```bash
  python3 access_log_parser.py access.log --status 404
  ```

#### 引数

- `logfile`: (必須) 解析対象のアクセスログファイルパス。
- `--ip`: (任意) 抽出したいIPアドレスを指定します。
- `--status`: (任意) 抽出したいHTTPステータスコードを指定します。

**注意:** `--ip` と `--status` は同時に指定できません。

---
今後、より複雑なログ形式（Combined Log Formatなど）への対応や、集計機能の拡充を予定しています。
