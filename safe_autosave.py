# safe_autosave.py
# 提出用サンプル
# カレントディレクトリにテキストファイルを作成
# 環境依存なし・個人情報なし

import os

# 保存するテキスト
text_to_write = "こんにちは！Pythonで自動入力中です。"

# ファイル名（カレントディレクトリに保存）
file_name = "demo.txt"
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)

# ファイルを書き込む
with open(file_path, "w", encoding="utf-8") as f:
    f.write(text_to_write)

# 完了メッセージ
print(f"ファイル '{file_name}' が以下のフォルダに保存されました：")
print(os.path.dirname(file_path))
