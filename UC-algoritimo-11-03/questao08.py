compra = float(input("digite o total da compra:"))

if compra >= 100 and compra < 500:
  desconto = compra * 0.95
  print(f"sua compra sem desconto {compra} com desconto {desconto}")
elif compra >=500 and compra < 1000:
   desconto = compra * 0.80
   print(f"sua compra sem desconto {compra} com desconto {desconto}")
elif compra >=1000:
    desconto = compra * 0.75
    print(f"sua compra sem desconto {compra} com desconto {desconto}")
else:
   print(f"voce não tem disconto total é {compra}")






