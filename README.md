# python-toolkit

フォルダ構成

python-toolkit/
├── README.md               # リポジトリ全体の概要、環境構築方法
├── requirements.txt        # 必要なライブラリ一覧
├── .gitignore              # git管理から除外する設定（__pycache__やvenvなど）
│
├── data_processing/        # 【データ加工・整形】
│   ├── tsv_splitter/       # TSVファイル分割ツール
│   ├── format_converter/   # CSV/Excel/JSONなどの相互変換
│   └── cleaning/           # 異常値除去、表記揺れ修正など
│
├── data_analysis/          # 【データ分析】
│   ├── exploratory/        # 探索的データ分析（EDA）用テンプレート
│   ├── visualization/      # グラフ作成、レポート出力
│   └── statistics/         # 統計検定、相関分析など
│
├── infrastructure/         # 【インフラ構築・運用】
│   ├── aws_helpers/        # AWS操作（boto3）スクリプト
│   ├── log_parser/         # サーバーログの抽出・解析
│   └── ssh_automation/     # リモート操作、自動デプロイ関連
│
├── utils/                  # 【共通ユーティリティ】
│   ├── logger.py           # 共通のログ出力設定
│   ├── config_loader.py    # 設定ファイル(yaml/json)読み込み
│   └── file_handler.py     # 共通のファイル入出力処理
│
└── templates/              # 【雛形】
    └── basic_script.py     # 新しくツールを作る際のテンプレート