semana = []
soma = 0
for i in range(7):
    temperatura = float(input("Tenperatura do dia:"))
    semana.append(temperatura)
    soma+=temperatura
    media = soma / 7
print(f"lista da semana:{semana} ")
print(f"media:{media}")