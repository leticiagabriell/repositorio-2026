

n1 = float(input("digite um numero:"))
n2 = float(input("digite um numero:"))

def calcular(n1,n2):
    soma=n1+n2
    produto=n1*n2
    return soma,produto


resultado , resultado_p = calcular(n1,n2)

print(f"Soma: {resultado}")
print(f"Produto: {resultado_p}")




