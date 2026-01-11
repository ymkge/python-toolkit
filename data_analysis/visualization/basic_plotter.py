import pandas as pd
import argparse
import os
import sys
import matplotlib.pyplot as plt
import seaborn as sns

# プロジェクトルートをsys.pathに追加
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from utils.logger import get_logger

# ロガーを取得
logger = get_logger(__name__)

def create_plot(input_path: str, output_path: str, plot_type: str, x_col: str, y_col: str, hue_col: str = None):
    """
    CSVデータからグラフを生成し、画像として保存します。

    Args:
        input_path (str): 入力CSVファイルのパス。
        output_path (str): 出力画像ファイルのパス。
        plot_type (str): グラフの種類 ('bar' または 'scatter')。
        x_col (str): X軸に対応するカラム名。
        y_col (str): Y軸に対応するカラム名。
        hue_col (str, optional): 色分けに使用するカラム名。デフォルトはNone。
    """
    try:
        logger.info(f"'{input_path}' の読み込みを開始します。")
        df = pd.read_csv(input_path)
        logger.info(f"データ読み込み完了。データ数: {len(df)}件")

        # スタイルを設定
        sns.set_theme(style="whitegrid")
        plt.figure(figsize=(10, 6))

        logger.info(f"'{plot_type}' グラフの生成を開始します (X='{x_col}', Y='{y_col}').")

        if plot_type == 'bar':
            sns.barplot(data=df, x=x_col, y=y_col, hue=hue_col)
        elif plot_type == 'scatter':
            sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue_col)
        else:
            logger.error(f"エラー: 未知のグラフ種類 '{plot_type}'。'bar' または 'scatter' を指定してください。")
            return

        plt.title(f'{plot_type.capitalize()} Plot: {y_col} vs {x_col}')
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.xticks(rotation=45)
        plt.tight_layout() # ラベルが重ならないように調整

        plt.savefig(output_path)
        logger.info(f"グラフを '{output_path}' に保存しました。")

    except FileNotFoundError:
        logger.error(f"エラー: 入力ファイル '{input_path}' が見つかりません。")
        sys.exit(1)
    except KeyError as e:
        logger.error(f"エラー: 指定されたカラム '{e}' がファイル内に存在しません。")
        sys.exit(1)
    except Exception as e:
        logger.error(f"グラフ生成中に予期せぬエラーが発生しました: {e}")
        sys.exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CSVデータから基本的なグラフを生成するツール')
    parser.add_argument('input', help='入力CSVファイルのパス')
    parser.add_argument('output', help='出力画像ファイルのパス (例: my_plot.png)')
    parser.add_argument('--type', required=True, choices=['bar', 'scatter'], help='生成するグラフの種類')
    parser.add_argument('--x', required=True, help='X軸として使用するカラム名')
    parser.add_argument('--y', required=True, help='Y軸として使用するカラム名')
    parser.add_argument('--hue', default=None, help='色分けに使用するカラム名 (オプション)')

    args = parser.parse_args()

    create_plot(args.input, args.output, args.type, args.x, args.y, args.hue)
