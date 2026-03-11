Aluno = {}

Aluno ["nome"] = input ("Qual o seu nome:")
Aluno ["n1"] = float(input ("digite a primeira nota:"))
Aluno ["n2"] = float(input ("digite a segunda nota:"))
soma = Aluno ["n1"] + Aluno ["n2"]
media = soma / 2

Aluno ["media"] = media

if media >= 7:
    print("aluno aprovado")
elif media >=5:
    print(" aluno em recuperação")
else:
    print("aluno reprovado")


print("Nome:", Aluno["nome"])
print("nota 01", Aluno["n1"])
print("nota 02", Aluno["n2"])
print(f"a media do aluno foi {media}")
