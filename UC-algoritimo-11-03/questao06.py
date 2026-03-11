idade = int(input("digite sua idade:"))


if idade < 12:
    print("voce esta classificado em infantil")
elif idade >=12 and idade < 18:
    print("voce esta classificado em juvenil")
elif idade >=18 and idade <60:
    print("voce esta classificado em Adulto")
else:
    print("voce esta classificado em senior")