# 身長を入力させる
h = float(input("身長は？")) / 100.0
# 体重を入力させる
w = float(input("体重は？"))
# 上２つで得た数値で計算
bmi = w / (h * h)
# 計算結果の表示
print("あなたのBMI値は", bmi, "です。")
