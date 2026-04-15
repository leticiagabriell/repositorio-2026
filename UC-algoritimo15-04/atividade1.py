def calcular():
    try:
        preco1=float(input("digite o valor:"))
        preco2=float(input("digite o valor:"))

        total= preco1 + preco2

        print(f"o total é :{total}")

    except ValueError:
        print("digite somente numeros")
        
calcular()