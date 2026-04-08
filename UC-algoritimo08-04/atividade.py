n = int(input())
r = int(input())
p = int(input())

total = n
dias = 0 

while total < p:
    novos = n*(r**dias)
    total +=novos
    dias += 1

print(dias)