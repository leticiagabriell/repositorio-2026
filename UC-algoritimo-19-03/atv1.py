pontos = int(input("digite a quantidade de seus ponto:"))
derrota = int(input("digite a quantidade de derrotas:"))

def rank_jogador(pontos, derrotas):
    saldo = pontos - (derrotas * 10)
    
    if saldo <0:
        print("banido")
    elif saldo < 100:
        print("voce é broze")
    elif saldo <300:
        print("voce é prata")
    elif saldo >=600:
        print("voce é diamante")
    
        
rank_jogador(pontos,derrota)
    