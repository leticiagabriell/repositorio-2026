produto_p = float(input("Qual é o valor de um produto: "))

if produto_p > 500:
    total = produto_p * 0.80 
elif produto_p >= 200:
    total = produto_p * 0.90 
else:
    total = produto_p 

print(f"Valor sem desconto: {produto_p}")
print(f"Valor com desconto: {total}")
