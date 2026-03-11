numero=int(input("digite o valor do deposito:"))

while numero != 0 :
    if numero <0:
       numero=int(input("digite o valor do deposito:"))
       continue

    deposito+=numero
    numero=int(input("digite o valor do deposito:"))
print("valor total dos depositos]",deposito)
