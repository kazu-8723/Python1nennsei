# lesson16_tax.pyをインポート as taxとすることでモジュール名を省略名で書くことが可能
import lesson16_tax as tax

print(tax.postTaxPrice(120), "円")
print(tax.postTaxPrice(128), "円")
# print(lesson16_tax.postTaxPrice(980), "円")
