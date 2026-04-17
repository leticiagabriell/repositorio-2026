frase = input("Digite uma frase para análise: ").lower()
vogais = "aeiou"
contador = 0
for letra in frase:
        if letra in vogais:
            contador += 1

print(f"Total de vogais encontradas: {contador}")
