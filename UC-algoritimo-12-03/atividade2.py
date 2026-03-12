horas = float(input("digite suas horas de trabalho:"))
hora = float(input("digite o valor que voce ganha:"))

def calcularsalario(horas,valor):
    salario = horas * hora
    return salario


resultado= calcularsalario(horas,hora)

print(f"salario total: {resultado}")




