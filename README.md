# Python Toolkit

このリポジトリは、データ処理、分析、インフラ管理など、様々な場面で役立つPythonスクリプトやツールをまとめたツールキットです。

## 概要

日常的な作業や定型業務を自動化・効率化するための、再利用可能なコンポーネントを提供することを目的としています。各ツールは独立して使用することも、組み合わせて使用することも可能です。

## 環境構築

1.  **リポジリトのクローン**
    ```bash
    git clone https://github.com/your-username/python-toolkit.git
    cd python-toolkit
    ```

2.  **仮想環境の作成（推奨）**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **依存ライブラリのインストール**
    このツールキットに必要なライブラリをインストールします。
    ```bash
    pip install -r requirements.txt
    ```
    **注意:** `python3` コマンドがHomebrewのPython環境を指していない場合、`export PATH="/opt/homebrew/bin:$PATH"` のようにPATH環境変数を設定するか、`/opt/homebrew/bin/python3` を直接指定して実行してください。

## ツール一覧

各カテゴリの詳細については、それぞれのディレクトリにある `README.md` を参照してください。

- **[データ加工・整形 (Data Processing)](./data_processing/README.md)**
  - 生データを分析に適した形式に変換するツール群です。
  - 実装済みツール: `tsv_splitter` (TSVファイル分割), `csv_to_json` (CSV→JSON変換), `json_to_csv` (JSON→CSV変換)

- **[データ分析 (Data Analysis)](./data_analysis/README.md)**
  - データを分析し、可視化するためのツールやテンプレートです。
  - 実装済みツール: `basic_plotter` (棒グラフ, 散布図, ヒストグラム, 箱ひげ図生成)

- **[インフラ構築・運用 (Infrastructure)](./infrastructure/README.md)**
  - サーバーやクラウド環境の運用を自動化するスクリプト群です。
  - 実装済みツール: `access_log_parser` (Apacheアクセスログ解析)

- **[共通ユーティリティ (Utils)](./utils/README.md)**
  - 各ツールから共通して利用される、ロギングや設定ファイル読み込みなどの補助機能です。
  - 実装済みツール: `config_loader` (YAML設定ファイル読み込み), `logger` (共通ログ出力)

## 基本的な使い方

各ツールの詳細な使い方は、それぞれのディレクトリにある `README.md` を参照してください。

例として、`tsv_splitter` を使ってTSVファイルを分割する方法を示します。

1.  `data_processing/tsv_splitter` ディレクトリに移動します。
    ```bash
    cd data_processing/tsv_splitter
    ```

2.  `tsv_split.py` を実行します。第一引数に対象のファイル名を指定します。
    ```bash
    # 30,000行ごとに分割する場合 (デフォルト)
    python3 tsv_split.py your_large_file.tsv

    # 100,000行ごとに分割する場合
    python3 tsv_split.py your_large_file.tsv 100000
    ```
    実行後、`your_large_file_split_result_1.tsv`, `_2.tsv`, ... のようなファイルが生成されます。

---

## Next Steps (次回の作業候補)

以下のいずれかの方向性で開発を進めることができます。

1.  **既存ツールの機能拡充**:
    *   `access_log_parser`でより詳細な集計（例: リクエストパスごとのアクセス数）に対応する。
    *   `tsv_splitter`にCSV形式の分割機能を追加する。

2.  **新しいツールの実装**:
    *   `utils`に共通のファイル操作をまとめた`file_handler.py`を作成する。
    *   `data_processing/cleaning`に欠損値処理ツールを作成する。

3.  **全く新しいカテゴリやツールの追加**:
    *   例えば、機械学習モデルの簡単な学習と評価を行う `machine_learning` カテゴリを追加する。

ご希望に応じて、これらの作業を進めることができます。
