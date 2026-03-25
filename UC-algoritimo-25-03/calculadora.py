def calculadora(a,b):

    print("[1] adição")
    print("[2] subitracao")
    print("[3] mutiplicação")
    print("[4] divisão")
    print("[0] sair")
    opcao = int(input("digite sua opição:"))
    match opcao:
      case 1:
        return a + b
      case 2:
        return a - b
      case 3:
        return a * b
      case 4:
         return a / b
      case 0:
        print("saindo...")
      case _:
        print("apção invalida")
    





    