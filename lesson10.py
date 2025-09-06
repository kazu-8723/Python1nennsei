a = "100"
print(int(a) + 23)

a = "100"
b = "こんにちは"
# 変数を正しく数値に変換できるかチェック
print(a.isdigit())
print(b.isdigit())

b = "こんにちは"
# ｂが数値ならb+23,そうでなければ否定
if b.isdigit():
    print(int(b) + 23)
else:
    print("数値ではない")
