senha = input("digite sua senha:")
tamanho = len(senha)
if tamanho > 8:
    print("senha valida")
else:
    print("senha não valida ( no minimo 8 digitos)")