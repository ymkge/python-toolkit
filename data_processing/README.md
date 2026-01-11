# データ加工・整形 (Data Processing)

このディレクトリには、生データを分析や機械学習に適した形式に変換するための、データ加工や整形に関するツールを格納します。

## 機能一覧

- **[ファイル分割 (File Splitter)](./tsv_splitter/README.md)**
  - `tsv_splitter`: 巨大なTSVファイルを指定した行数で分割します。（実装済み）

- **[フォーマット変換 (Format Converter)](./format_converter/README.md)**
  - CSV、Excel、JSONなど、異なるデータ形式を相互に変換するツール群です。
  - `csv_to_json`: CSVファイルをJSONファイルに変換します。（実装済み）

- **データクリーニング (Data Cleaning)**
  - 欠損値の補完や削除、異常値の検出と除去、テキストデータの表記揺れ（例: "株式会社"と"(株)"）の修正など、データの品質を向上させるためのスクリプトです。（未実装）