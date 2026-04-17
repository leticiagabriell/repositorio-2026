try:
    n1 = int(input("digite um numero:"))
    n2 = int(input("digite um numero:"))
    operacao=input("qual operação vc quer fazer(+,-,*,/)")

    if operacao == "+":
        soma=n1+n2
        print(f"a soma é {soma}")
    elif operacao == "-":
        subitracao=n1-n2
        print(f"a subtração é {subitracao}")
    elif operacao == "*":
        mutiplicacao = n1*n2
        print(f"a mutiplicação é {mutiplicacao}")
    elif operacao == "/":
        if n2!= 0:
            divicao=n1/n2
            print(f"a divisão é {divicao}")
    else:
        print("opição invalida")
except ValueError:
    print("Erro:Digite somente numeros")