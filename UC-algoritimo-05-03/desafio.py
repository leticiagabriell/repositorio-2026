import random
lista_D = [34,37,17,47,67,19]
print(lista_D)

lista_D.sort()
print("ordem crecente():",lista_D)

lista_D.sort(reverse=True)
print("ordem decrecente():",lista_D)

random.shuffle(lista_D)
print("lista embaralhada:",lista_D)