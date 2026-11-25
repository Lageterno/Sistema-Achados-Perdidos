from cadastro import cadastrar_objeto
from consultas import listar_objetos
from atualizacoes import atualizar_objeto
from exclusoes import excluir_objeto

def mostrar_menu():
    while True:
        print("==============================")
        print("SISTEMA DE ACHADOS E PERDIDOS")
        print("==============================")
        print("1 - Cadastrar objeto")
        print("2 - Listar objetos")
        print("3 - Atualizar objeto")
        print("4 - Excluir objeto")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_objeto()

        elif opcao == "2":
            listar_objetos()
            input("\nPressione Enter para voltar ao menu...")

        elif opcao == "3":
            atualizar_objeto()
            input("\nPressione Enter para voltar ao menu...")
           

        elif opcao == "4":
            excluir_objeto()
            input("\nPressione Enter para voltar ao menu...")

        elif opcao == "5":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")
            
mostrar_menu()