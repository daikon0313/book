# names = ["齋藤", "佐藤", "田中"]
# i = 1
# for n in names:
#     print(f"{i}番目の名前は{n}です")
#     i += 1

# names = ["齋藤", "佐藤", "田中"]
# for i, n in enumerate(names, start=1):
#     print(f"{i}番目の名前は{n}です")

# hiragana = ["あ", "い", "う", "え", "お"]
# alphabet = ["a", "b", "c", "d", "e"]

# for h, a in zip(hiragana, alphabet):
#     print(f"{h}は{a}です")

hiragana = ["あ"]
alphabet = ["A", "B", "C", "D"]

for h, a in zip(hiragana, alphabet, strict=False):
    print(f"{h}は{a}です")