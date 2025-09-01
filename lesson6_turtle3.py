# タートルグラフィックス使用準備
from turtle import *
# 亀登場
shape("turtle")
# 色の指定
col = ["orange", "limegreen", "gold", "plum", "tomato"]
# 以下3行を5回繰り返す
for i in range(5):
# 線の色の変更
    color(col[i])
# 200直進
    forward(200)
# 144度左折
    left(144)
# 終了
done()
