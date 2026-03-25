def media_total():
    n1 = float(input("digite sua nota:"))
    n2 = float(input("digite sua nota:"))

    total = 0 
    notas = [n1,n2]
    for num  in notas:
        total += num
        media = total / len(notas)
        nota_max = max(notas)      
        nota_min = min(notas) 

    return total, media, nota_max, nota_min
resultado = media_total()

print(resultado)