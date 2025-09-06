# 関数の作成
def sayhello():
# 関数内の設定
    print("こんにちは")
# 関数の内部を呼び出す
sayhello()


# 引数のみある関数の作成
def sayhello2(name):
# 関数内の設定
    print("こんにちは、" + name + "さん。")
# 関数の内部を呼び出す
sayhello2("ピカチュウ")


import random
# 関数作成
def omikuji():
# リスト作成
    kuji = ['大吉', '中吉', '小吉', '凶']
# リスト内からランダムで選ばれたものを戻り値として返す
    return random.choice(kuji)
kekka = omikuji()
print("結果は", kekka, "です。")
