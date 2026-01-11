import yaml
from typing import Dict, Any

def load_config(file_path: str = 'config.yaml') -> Dict[str, Any]:
    """
    YAML設定ファイルを読み込み、辞書として返します。

    Args:
        file_path (str): 読み込む設定ファイルのパス。
                         デフォルトは 'config.yaml' です。

    Returns:
        Dict[str, Any]: 設定内容を格納した辞書。

    Raises:
        FileNotFoundError: 指定されたファイルが見つからない場合。
        yaml.YAMLError: ファイルのパースに失敗した場合。
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
            if config is None:
                return {}
            return config
    except FileNotFoundError:
        print(f"エラー: 設定ファイル '{file_path}' が見つかりません。")
        raise
    except yaml.YAMLError as e:
        print(f"エラー: 設定ファイル '{file_path}' の読み込みに失敗しました。")
        print(e)
        raise

if __name__ == '__main__':
    # --- このスクリプトを直接実行した際のテスト用コード ---
    
    # テスト用のダミー設定ファイルを作成
    test_config_content = """
    # API設定
    api:
      key: "your_api_key_here"
      endpoint: "https://api.example.com/v1"

    # データベース設定
    database:
      host: "localhost"
      port: 5432
      user: "admin"
      password: "password"
    
    # ファイルパス設定
    paths:
      input_dir: "/path/to/input"
      output_dir: "/path/to/output"
    """
    test_file_name = 'test_config.yaml'
    with open(test_file_name, 'w', encoding='utf-8') as f:
        f.write(test_config_content)

    print(f"'{test_file_name}' を使って設定読み込みのテストを実行します。")
    
    try:
        # 正常系のテスト
        config_data = load_config(test_file_name)
        print("\n--- 読み込み成功 ---")
        print(config_data)
        
        # APIキーの取得例
        print("\n--- 値の取得例 ---")
        api_key = config_data.get('api', {}).get('key')
        print(f"API Key: {api_key}")

        # 存在しないキーの取得例
        non_existent_value = config_data.get('server', {}).get('host', 'default-host')
        print(f"存在しないキー (server.host): {non_existent_value}")

    except (FileNotFoundError, yaml.YAMLError) as e:
        print(f"\nテスト中にエラーが発生しました: {e}")

    finally:
        # テスト用ファイルを削除
        import os
        if os.path.exists(test_file_name):
            os.remove(test_file_name)
            print(f"\nテスト用の '{test_file_name}' を削除しました。")
