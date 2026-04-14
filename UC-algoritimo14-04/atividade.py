
def soma(a,b):

    try:
        return a + b
        
    except TypeError:
        print("Entrada inválida")
        return 0
res1 = soma(10, 20)
print(f"Resultado: {res1}")