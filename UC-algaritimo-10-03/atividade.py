paciente = {}

paciente ["nome"] = input ("Qual o seu nome:")
paciente ["idade"] = int(input ("Quantos anos voce tem:"))
paciente ["peso"] = float(input ("digite seu peso(kg):"))
paciente ["altura"] = float(input ("digite seu altura(m):"))

imc = paciente ["peso"] / (paciente["altura"] ** 2)

paciente ["imc"] = imc

print("\n Dados")
print("Nome:", paciente["nome"])
print("idade:", paciente["idade"])
print("peso:", paciente["peso"])
print("altura:", paciente["altura"])
print("imc:", round (paciente["altura"],2))