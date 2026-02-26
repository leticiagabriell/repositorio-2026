resp = input("voce vai passar de ano s/n:").strip().lower()
#resposta= bool(resp)
#resposta = (resp == "s")
resposta= resp in("sim","s","si","ok" )


print("resposta ",resp)
print("resultado ",resposta)