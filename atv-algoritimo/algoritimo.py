lista = []
emprestados = []

while True:
    print("==== MENU ====")
    print("[1] Cadastrar livros")
    print("[2] Listar livros")
    print("[3] Emprestar livros")
    print("[4] Devolver livros")
    print("[5] Ver emprestados")
    print("[0] Sair")

    opcao = int(input("Escolha a opção: "))

    match opcao:
        case 1:
            nome = input("Digite o nome do livro: ")
            autor = input("Digite o autor: ")
            ano = int(input("Digite o ano: "))

            lista.append(nome)

            print("Cadastro feito com sucesso")

        case 2:
            print("Livros cadastrados:")
            for livro in lista:
                print(livro)

        case 3:
            livro = input("Digite o livro para emprestar: ")
            if livro in lista:
                lista.remove(livro)
                emprestados.append(livro)
                print("Livro emprestado")
            else:
                print("Livro não encontrado")

        case 4:
            livro = input("Digite o livro devolvido: ")
            if livro in emprestados:
                emprestados.remove(livro)
                lista.append(livro)
                print("Livro devolvido")
            else:
                print("Esse livro não está emprestado")

        case 5:
            print("Livros emprestados:")
            for livro in emprestados:
                print(livro)

        case 0:
            print("Saindo...")
            break

        case _:
            print("Opção inválida")
