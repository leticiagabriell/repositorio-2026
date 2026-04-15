def calculos():
   notas = []
   try:
      for i in range(1,4):
          nota = float(input(f"Digite a nota {i}: "))
          notas.append(nota)

      media = sum(notas) / len(notas)
      print(f"A média final é: {media:.2f}")

   except ValueError:
      print("digite somente numeros")

calculos()
