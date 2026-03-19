saldo = float(input("digite o valor a sacar:"))
saque = float(input("digite o valor a sacar:"))

def saldo_final(saldo, saque):
   
   if saque > saldo:
      return "Saldo insuficiente"
   
    if saque > 1000:
        taxa = saque * 0.02
        saldo -= (saque + taxa)
    else:
      saldo -= saque

return saldo

print("O resultado é", saldo_final(saldo, saque))
   
   
