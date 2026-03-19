saldo = 5000
saque = float(input("digite o valor a sacar:"))

def saldo_final(saldo, saque):
   
   if saque >saldo:
      print("saldo indefinido")
      return saldo
   saldo_t = saldo - saque
   if saque <= saldo_t and saque > 100:
      saldo_t = saldo_t * 0.98
   return saldo_t
   
saldo_final(saldo, saque)
print(f"saldo atual:{saldo_t}")
   
