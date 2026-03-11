contato = {
    "@camila" : "camila",
    "@paola" : "paolla",
    "@shoron" : "sheron",
    "@bruna" : "bruna"
}

#obter chave
print("chaves: ")
for insta in contato.keys():
    print(insta)

#obter valores
print("\n valores:")
for nome in contato.values():
    print(nome)

#obter pares
print("\n pares:")
for insta, nome in contato in contato.items():
    print(f"{insta} --> {nome}")
    
contato = {
    "@camila" : 1.70,
    "@paola" : 1.80,
    "@shoron" : 1.55,
    "@bruna" : 1.60 
}
print("ordenando por chave:")
for insta in  sorted(contato.Keys()):
     print(f"{insta} --> {contato [insta]:.2f}m")

from operator import itemgetter
print("\n ordenado por valor (altura):")
for insta,estatura in sorted (contato.items(), Key = itemgetter(1)):
   print(f"{insta} --> {estatura:.2f}m")
