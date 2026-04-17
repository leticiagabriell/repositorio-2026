def calculo():
    try:
        altura =float(input("Digite sua altura:"))
        peso = float(input("Digite seu peso:"))
        imc = peso / (altura * altura)
        
        if imc < 18.5:
            print("abaixo do peso")
        elif imc < 24.4:
            print("peso normal")
        elif imc <= 29.9:
            print("sobrepeso")
        else:
            print("obeso")
    except ValueError:
            print("Erro: Você deve digitar um número inteiro válido.") 

calculo()