n1=int(input("digite um numero:"))
if n1<0:
    print("numero invalido")
elif n1 %2 ==0:
    quadrado=n1*n1
    print(f"seu numero é par sendo o quadrado {quadrado}")
else:
    cubo=n1*n1*n1
    print(f"seu numero é impar sendo o cubo é {cubo}")