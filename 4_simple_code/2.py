from pathlib import Path

# ファイル一覧を取得
# txt_folder = Path('./sample_docs')
# txt_files = list(txt_folder.iterdir())
# print(txt_files)

# 絶対パスの取得
# txt_folder = Path('./sample_docs')
# abs_path = txt_folder.resolve()
# print(abs_path)
# print(type(abs_path))

# 名前の取得
# txt_folder = Path('./sample_docs')
# txt_file = Path('./sample_docs/sample.txt')
# print(txt_folder.name)
# print(txt_file.name)

# パスの結合
# footer_path = Path("./sample_docs") / "sample.txt"
# print(footer_path)
# print(type(footer_path))

# パスの確認
# from pathlib import Path

# footer_path = Path("./sample_docs/sample.txt")
# print(footer_path.exists())

# ファイルの作成
# footer_path = Path("./sample_docs/sample_2.txt")
# footer_path.touch()

# ファイルの削除
# footer_path = Path("./sample_docs/sample_2.txt")
# footer_path.unlink(missing_ok=True)

# フォルダの作成
# outputs_path = Path("./outputs")
# outputs_path.mkdir(exist_ok=True)

# フォルダの削除
# outputs_path = Path("./outputs")
# outputs_path.rmdir()

import json

# json_str = '{"name": "齋藤", "age": 23}'
# dict_obj = json.loads(json_str)

# print(dict_obj)

# with open("./sample_docs/user.json") as f:
#     user = json.load(f)

# print(user)
# print(type(user))

user = {
    "id": "A001",
    "age": None,
    "is_active": True,
    "point": 2,
}

with open("./sample_docs/user_write.json", "w") as f:
    json_str = json.dump(user, f)
