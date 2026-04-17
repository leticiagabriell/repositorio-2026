vendas = [10, 15, 20, 25, 30, 35, 40]
soma = 0

for valor in vendas:
    if valor % 2 == 0:
        soma += valor

print(f"A soma dos valores pares é: {soma}")
