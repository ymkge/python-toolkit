import logging
import sys

# --- 定数 ---
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    設定済みのロガーを取得します。

    - ログはコンソールにストリーミングされます。
    - フォーマット: 'タイムスタンプ - ロガー名 - ログレベル - メッセージ'

    Args:
        name (str): ロガーの名前。通常は __name__ を渡します。
        level (int): 出力するログのレベル (例: logging.INFO, logging.DEBUG)。
                     デフォルトは logging.INFO です。

    Returns:
        logging.Logger: 設定済みのロガーオブジェクト。
    """
    # ロガーを取得
    logger = logging.getLogger(name)
    
    # ロガーが既に設定済みであれば、重複してハンドラを追加しない
    if logger.hasHandlers():
        return logger

    logger.setLevel(level)

    # ハンドラ（ログの出力先）を設定
    handler = logging.StreamHandler(sys.stdout) # コンソールに出力
    handler.setLevel(level)

    # フォーマッタ（ログの書式）を設定
    formatter = logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT)
    handler.setFormatter(formatter)

    # ロガーにハンドラを追加
    logger.addHandler(handler)

    return logger

if __name__ == '__main__':
    # --- このスクリプトを直接実行した際のテスト用コード ---

    # 'main_test' という名前でロガーを取得
    main_logger = get_logger('main_test', level=logging.DEBUG)

    print("--- ログ出力テスト ---")
    main_logger.debug("これはデバッグメッセージです。詳細な情報。")
    main_logger.info("これは情報メッセージです。処理の進捗など。")
    main_logger.warning("これは警告メッセージです。注意が必要な事象。")
    main_logger.error("これはエラーメッセージです。処理の実行に失敗。")
    main_logger.critical("これは致命的なエラーメッセージです。システムが停止する可能性。")

    # 別のモジュールから呼ばれた場合をシミュレート
    print("\n--- 別のモジュールでの利用をシミュレート ---")
    
    class SubModule:
        def __init__(self):
            # モジュール名を指定してロガーを取得
            self.logger = get_logger(self.__class__.__name__)

        def do_something(self):
            self.logger.info("SubModuleの処理を開始します。")
            # ... 何らかの処理 ...
            self.logger.info("SubModuleの処理が完了しました。")

    sub = SubModule()
    sub.do_something()

    # 同じ名前で再度ロガーを取得しても、設定は重複しないことを確認
    print("\n--- ロガーの再取得テスト ---")
    another_logger = get_logger('main_test')
    another_logger.info("このメッセージは1回だけ表示されるはずです。 ")
