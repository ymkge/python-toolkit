import argparse
import os
import sys
import re
from collections import Counter

# プロジェクトルートをsys.pathに追加
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from utils.logger import get_logger

# ロガーを取得
logger = get_logger(__name__)

# Apache Common Log Format の正規表現
# 例: 127.0.0.1 - - [10/Oct/2000:13:55:36 +0000] "GET /apache_pb.gif HTTP/1.0" 200 2326
LOG_REGEX = re.compile(r'^(?P<ip>[\d\.]+) \S+ \S+ \[(?P<datetime>[^\]]+)\] "(?P<request>[^"]+)" (?P<status>\d{3}) (?P<size>\d+)$')

def parse_log_file(log_path: str, filter_ip: str = None, filter_status: int = None, report_by: str = 'ip'):
    """
    アクセスログファイルを解析し、情報を集計・表示します。

    Args:
        log_path (str): 解析対象のログファイルパス。
        filter_ip (str, optional): 抽出するIPアドレス。デフォルトはNone。
        filter_status (int, optional): 抽出するHTTPステータスコード。デフォルトはNone。
        report_by (str, optional): 集計キー ('ip' または 'path')。デフォルトは 'ip'。
    """
    try:
        logger.info(f"ログファイル '{log_path}' の解析を開始します。")
        
        matched_lines = []
        with open(log_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = LOG_REGEX.match(line.strip())
                if not match:
                    logger.warning(f"フォーマットに一致しない行をスキップしました: {line.strip()}")
                    continue
                
                log_data = match.groupdict()
                
                # リクエストパスを抽出
                request_parts = log_data['request'].split()
                log_data['path'] = request_parts[1] if len(request_parts) > 1 else ''

                # フィルタリング
                if filter_ip and log_data['ip'] != filter_ip:
                    continue
                if filter_status and int(log_data['status']) != filter_status:
                    continue
                
                matched_lines.append(log_data)

        if not matched_lines:
            logger.info("指定された条件に一致するログが見つかりませんでした。")
            return

        logger.info(f"合計 {len(matched_lines)} 件のログが見つかりました。")
        
        # 結果の集計と表示
        print("\n--- 解析結果 ---")
        if filter_ip:
            print(f"IPアドレス '{filter_ip}' のアクセス記録:")
            for log in matched_lines:
                print(f"  - Time: {log['datetime']}, Request: {log['request']}, Status: {log['status']}")
        
        elif filter_status:
            print(f"ステータスコード '{filter_status}' のアクセス記録:")
            ip_counter = Counter(log['ip'] for log in matched_lines)
            for ip, count in ip_counter.most_common():
                print(f"  - IP: {ip}, 回数: {count}")

        else:
            if report_by == 'path':
                # リクエストパスごとのアクセス回数を集計
                print("リクエストパスごとのアクセス回数:")
                path_counter = Counter(log['path'] for log in matched_lines)
                for path, count in path_counter.most_common():
                    print(f"  - {path}: {count}回")
            else: # report_by == 'ip' (デフォルト)
                # IPアドレスごとのアクセス回数を集計
                print("IPアドレスごとのアクセス回数:")
                ip_counter = Counter(log['ip'] for log in matched_lines)
                for ip, count in ip_counter.most_common():
                    print(f"  - {ip}: {count}回")

    except FileNotFoundError:
        logger.error(f"エラー: ログファイル '{log_path}' が見つかりません。")
        sys.exit(1)
    except Exception as e:
        logger.error(f"解析中に予期せぬエラーが発生しました: {e}")
        sys.exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Apacheアクセスログを解析するツール')
    parser.add_argument('logfile', help='解析対象のログファイルパス')
    
    # 集計方法のオプション
    parser.add_argument('--report-by', default='ip', choices=['ip', 'path'], help="集計キーを選択 ('ip' または 'path')")

    # フィルタリング用のオプションをグループ化
    filter_group = parser.add_mutually_exclusive_group()
    filter_group.add_argument('--ip', help='特定のIPアドレスでフィルタリング')
    filter_group.add_argument('--status', type=int, help='特定のHTTPステータスコードでフィルタリング')

    args = parser.parse_args()

    parse_log_file(args.logfile, args.ip, args.status, args.report_by)