def div(a,b):
    try:
        return a / b
        
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero!")
        return 0
    
print(f"Resultado: {div(10, 0)}")