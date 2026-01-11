# Python Toolkit

このリポジトリは、データ処理、分析、インフラ管理など、様々な場面で役立つPythonスクリプトやツールをまとめたツールキットです。

## 概要

日常的な作業や定型業務を自動化・効率化するための、再利用可能なコンポーネントを提供することを目的としています。各ツールは独立して使用することも、組み合わせて使用することも可能です。

## 環境構築

1.  **リポジトリのクローン**
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

## ツール一覧

各カテゴリの詳細については、それぞれのディレクトリにある `README.md` を参照してください。

- **[データ加工・整形 (Data Processing)](./data_processing/README.md)**
  - 生データを分析に適した形式に変換するツール群です。
  - 機能例: ファイル分割、フォーマット変換、データクリーニング

- **[データ分析 (Data Analysis)](./data_analysis/README.md)**
  - データを分析し、可視化するためのツールやテンプレートです。
  - 機能例: 探索的データ分析、グラフ作成、統計検定

- **[インフラ構築・運用 (Infrastructure)](./infrastructure/README.md)**
  - サーバーやクラウド環境の運用を自動化するスクリプト群です。
  - 機能例: AWS操作、ログ解析、SSH経由での自動デプロイ

- **[共通ユーティリティ (Utils)](./utils/README.md)**
  - 各ツールから共通して利用される、ロギングや設定ファイル読み込みなどの補助機能です。

## 基本的な使い方

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
