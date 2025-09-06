# 関数作成(priceが引数)
def postTaxPrice(price):
# 引数をもとに計算、ansが戻り値
    ans = price * 1.1
    return ans

print(postTaxPrice(120), "円")
print(postTaxPrice(128), "円")
print(postTaxPrice(980), "円")
