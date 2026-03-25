def soma_total(*numeros):
    total = 0 
    for num  in numeros:
        total += num
    return total

print(soma_total(1,2,3))
print(soma_total(10,20,30,40,50))
print(soma_total())