import pandas as pd
import argparse
import os
import sys

# プロジェクトルートをsys.pathに追加して、utilsをインポート可能にする
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from utils.logger import get_logger

# このモジュール用のロガーを取得
logger = get_logger(__name__)

def convert_json_to_csv(input_path: str, output_path: str, orientation: str = 'records'):
    """
    JSONファイルを読み込み、CSVファイルに変換して保存します。

    Args:
        input_path (str): 入力JSONファイルのパス。
        output_path (str): 出力CSVファイルのパス。
        orientation (str): JSONのフォーマット形式。pandas.read_jsonを参照。
                           デフォルトは 'records'。
    """
    try:
        logger.info(f"'{input_path}' の読み込みを開始します。")
        # JSONの構造に合わせて 'orient' を指定
        df = pd.read_json(input_path, orient=orientation)
        logger.info("JSONファイルの読み込みが完了しました。")

        logger.info("CSVへの変換を開始します。")
        # index=False で行番号を出力しない
        df.to_csv(output_path, index=False, encoding='utf-8-sig')
            
        logger.info(f"変換完了。'{output_path}' に保存しました。")

    except FileNotFoundError:
        logger.error(f"エラー: 入力ファイル '{input_path}' が見つかりません。")
        sys.exit(1)
    except ValueError as e:
        logger.error(f"JSONの形式が正しくない可能性があります。'{orientation}' 形式で読み込めませんでした。: {e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"変換中に予期せぬエラーが発生しました: {e}")
        sys.exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='JSONファイルをCSVファイルに変換するツール')
    parser.add_argument('input', help='入力JSONファイルのパス')
    parser.add_argument('output', help='出力CSVファイルのパス')
    parser.add_argument(
        '--orientation', 
        default='records', 
        choices=['split', 'records', 'index', 'columns', 'values', 'table'],
        help="JSONの入力形式 (pandas.read_jsonのorientオプション)"
    )

    args = parser.parse_args()

    convert_json_to_csv(args.input, args.output, args.orientation)
