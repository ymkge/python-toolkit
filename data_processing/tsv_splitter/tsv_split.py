import pandas as pd
import sys
import os
import csv

def split_tsv(input_file):
    rows_per_file = 100000 
    max_char_limit = 45000 

    if not os.path.exists(input_file):
        print(f"エラー: ファイル '{input_file}' が見つかりません。")
        return

    base_name = os.path.splitext(os.path.basename(input_file))[0]

    try:
        # 修正：engine='python' を使うため low_memory=False を削除
        reader = pd.read_csv(
            input_file, 
            sep='\t', 
            chunksize=rows_per_file, 
            quoting=csv.QUOTE_NONE,
            on_bad_lines='warn',    # 不正行があればターミナルに表示されます
            skip_blank_lines=False, # 空行を数えに含める
            engine='python'
        )
        
        total_processed_rows = 0
        for i, chunk in enumerate(reader):
            # 文字数制限を適用
            chunk = chunk.applymap(lambda x: str(x)[:max_char_limit] if isinstance(x, str) else x)
            
            output_file = f"{base_name}_split_result_{i+1}.tsv"
            # 出力時も引用符を付けず、タブ区切りを維持
            chunk.to_csv(output_file, sep='\t', index=False, encoding='utf-8-sig', quoting=csv.QUOTE_NONE)
            
            total_processed_rows += len(chunk)
            print(f"作成完了: {output_file} ({len(chunk)}行)")
        
        print(f"\n--- 最終集計 ---")
        print(f"Pythonが読み込んだデータ行数: {total_processed_rows}")
        print(f"ヘッダー(1行)を足した合計: {total_processed_rows + 1}")
            
    except Exception as e:
        print(f"実行エラー: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        split_tsv(sys.argv[1])
    else:
        print("使用法: python3 split_tsv.py [ファイル名.tsv]")