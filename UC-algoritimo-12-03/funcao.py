#sem fução
print("python é facil")
print("python é facil")
print("python é facil")


#com função
def exibirmensagem():
     print("ola,mundo")

exibirmensagem()

#função com parametro
def saudar(nome):
     print(f"ola,{nome}")

saudar("ana")
saudar("Bruna")


def exibirmensagem(nome,mensagem):
     print(f"{mensagem},{nome}")

exibirmensagem("ana","bom dia")

exibirmensagem(nome = "bruno",mensagem ="boa noite")
 
#função que retorna media
def calcularmedia(n1,n2):
     media = (n1+n2) / 2
     return media

resultado = calcularmedia(8.0,9.0)
print(f"media:{resultado}")

nome = input("digite seu nome:")
def exibirmensagem(nome):
    print(f"ola,{nome}")
    

exibirmensagem(nome)

