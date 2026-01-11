import pandas as pd
import argparse
import os
import sys

# プロジェクトルートをsys.pathに追加して、utilsをインポート可能にする
# このスクリプトは project_root/data_processing/format_converter/ から実行されることを想定
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from utils.logger import get_logger

# このモジュール用のロガーを取得
logger = get_logger(__name__)

def convert_csv_to_json(input_path: str, output_path: str, orientation: str = 'records', indent: int = 4):
    """
    CSVファイルを読み込み、JSONファイルに変換して保存します。

    Args:
        input_path (str): 入力CSVファイルのパス。
        output_path (str): 出力JSONファイルのパス。
        orientation (str): JSONのフォーマット形式。pandas.DataFrame.to_jsonを参照。
                           デフォルトは 'records'。
        indent (int): JSONのインデント数。デフォルトは 4。
    """
    try:
        logger.info(f"'{input_path}' の読み込みを開始します。")
        df = pd.read_csv(input_path)
        logger.info("CSVファイルの読み込みが完了しました。")

        logger.info(f"JSONへの変換を開始します (format: {orientation})。")
        # to_jsonは文字列を返すので、ファイルに書き込む
        json_data = df.to_json(orient=orientation, indent=indent, force_ascii=False)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(json_data)
            
        logger.info(f"変換完了。'{output_path}' に保存しました。")

    except FileNotFoundError:
        logger.error(f"エラー: 入力ファイル '{input_path}' が見つかりません。")
        sys.exit(1)
    except Exception as e:
        logger.error(f"変換中に予期せぬエラーが発生しました: {e}")
        sys.exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CSVファイルをJSONファイルに変換するツール')
    parser.add_argument('input', help='入力CSVファイルのパス')
    parser.add_argument('output', help='出力JSONファイルのパス')
    parser.add_argument(
        '--orientation', 
        default='records', 
        choices=['split', 'records', 'index', 'columns', 'values', 'table'],
        help="JSONの出力形式 (pandas.DataFrame.to_jsonのorientオプション)"
    )
    parser.add_argument(
        '--indent',
        type=int,
        default=4,
        help="JSON出力のインデント数"
    )

    args = parser.parse_args()

    convert_csv_to_json(args.input, args.output, args.orientation, args.indent)
