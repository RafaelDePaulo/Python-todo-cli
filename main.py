tarefas = []

while True:
    print("\n=== MENU ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Sair")
    print("4 - Remover tarefa")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")

    elif opcao == "2":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\nTarefas:")
            for i, tarefa in enumerate(tarefas):
                print(f"{i + 1}. {tarefa}")

    elif opcao == "3":
        print("Saindo do programa...")
        break

    elif opcao == "4":
        if len(tarefas) == 0:
            print("Não há tarefas para remover.")
        else:
            print("\nTarefas:")
            for i, tarefa in enumerate(tarefas):
                print(f"{i + 1}. {tarefa}")

            numero = int(input("Digite o número da tarefa a remover: "))
            tarefas.pop(numero - 1)
            print("Tarefa removida com sucesso!")

    else:
        print("Opção inválida. Tente novamente.")
