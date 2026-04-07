p =int(input("Quantidade de pao:"))
D =int(input("Quantidade de doces:"))
B =int(input("Qunatidade de bolos:"))

total = p * 1 + D * 2 + B *3

if total >=150:
   print( "B")
elif total >=120:
   print("D")
elif total >=100:
   print("P")
else:
   print("N")