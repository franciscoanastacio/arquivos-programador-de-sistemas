convidados = []
while True:
    print("""================ Menu ===============
          1 - Adicionar convidado
          2 - listar convidados
          3 - Consultar convidados
          4 - Remover convidado
          5 - Quantidade de convidados
          6 - Editar convidado
          0 - Sair\n""")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        # Adicionar convidado
        nome = input("digite o nome do convidado:")
        convidados.append(nome)
        print(f"{nome} foi adicionado com sucesso!\n")
    elif opcao == 2:
        # Listar convidados
        if not convidados:
            print("A lista de convidados está vazia.\n")
        else:
            print("\n---lista de convidados---")
            for i, convidado in enumerate(convidados,start=1):
                print(f"{i}.{convidados}")
                print("---------------------------\n")
    elif opcao == 3:
        # Consultar convidados
        nome = input("digite o nome do convidado a ser consultado")
        if nome in convidados:
            print(f"{nome} está na lista de convidados.\n")
        else:
            print(f"{nome} não está na lista de convidados.\n")
    elif opcao == 4:
        # Remover convidado
        nome = input("digite o nome do convidado a ser removido:")
        if nome in convidados:
            convidados.remove(nome)
            print(f"{nome} removido da lista de convidados.\n")
        else:
            print(f"{nome} não está na lista de convidados.\n")
    elif opcao == 5:
        # Quantidade de convidados
        print(f"quantidade de convidados: {len(convidados)}\n")
    elif  opcao == 6:
        # Editar convidado
        nome_antigo = input("digite o nome do convidado a ser editado:")
        if nome_antigo in convidados:
           nome_novo = input("digite o novo nome do convidado:")
           Index = convidados.index(nome_antigo)
           convidados[Index] = nome_novo
           print("{nome_antigo} foi atualizado para {nome_novo}.\n")
        else:
           print(f"{nome_antigo} não está na lista de convidados.\n")
         
    elif opcao == 0:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.\n")


