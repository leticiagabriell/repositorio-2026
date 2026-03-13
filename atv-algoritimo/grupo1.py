
usuario = input("Digite seu usuario: ")
senha = int(input("Digite sua senha: "))

while senha != "19012010" and usuario != "anakinskywalker":
    print("senha ou usuario incorreto")
    usuario = input("Digite seu usuario: ")
    senha = input("Digite sua senha: ")

print(f"Bem vindo {usuario}")