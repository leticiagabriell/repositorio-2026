import random

x = random.randint(1, 100)
tentativas = 0
acertou = False

while not acertou:
    try:
        numero = int(input("digite um numero: "))
        tentativas += 1
        
      
        if numero == x:
            print("acertou")
            acertou = True
        elif numero < x:
            print("muito baixo")
        else:
            print("muito alto")
            
    except ValueError:
        print("Entrada inválida! Digite apenas números.")
print(f"voce acertou com {tentativas} tentativas")