notas = [7.5,8.0,9.5,6.0,8,5]
print("notas:",notas)

print("Menor:", min(notas))
print("Maior:", max(notas))
print("soma:", sum(notas))
print("Media:", sum(notas) / len (notas))

nomes = ["Adriana","Breno","","Carla","Daniel"]
print("usando for simples:")
for nome in nomes:
    print(f"ola {nome}!")

print("\n usando enumerate:")
for indice,nome in enumerate(nomes):
    print(f"posição {indice}:{nome}")





original= ["A","B","C"]
copia = list(original)


print("original:", original)
print("copia:", copia)
print("são iguais:", original == copia)

copia.append("D")
print("original:", original)
print("copia:", copia)
print("são iguais:", original == copia)   