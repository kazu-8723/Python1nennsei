# 10回繰り返す
for i in range(10):
# 5×0~5×9の計算の表示
    print(5, "×", i, "=", 5*i)

scorelist = [64, 100, 81, 39, 47]
# リスト内の要素を繰り返す
for i in scorelist:
    print(i)

scorelist = [64, 100, 81, 39, 47]
# 0にリセット
total = 0
# リスト内の数値を１つずつ足していく
for i in scorelist:
    total = total + i
print(total)

# 0〜9を繰り返す
for i in range(10):
# 0〜9を繰り返す
    for j in range(10):
        print(j, "×", i, "=", j*i)
