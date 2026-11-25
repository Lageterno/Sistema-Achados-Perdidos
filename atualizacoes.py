import json

def atualizar_objeto():
    with open("banco_dados.json", "r", encoding="utf-8") as arquivo:
        objetos = json.load(arquivo)

    print("\n=== ATUALIZAR OBJETO ===")

    nome_busca = input("Digite o nome do objeto que deseja atualizar: ")

    encontrado = False

    for objeto in objetos:
        if objeto["nome"].lower() == nome_busca.lower():

            print("\nObjeto encontrado!")

            objeto["nome"] = input("Novo nome: ")
            objeto["categoria"] = input("Nova categoria: ")
            objeto["descricao"] = input("Nova descrição: ")
            objeto["local"] = input("Novo local: ")
            objeto["data"] = input("Nova data: ")
            objeto["tipo"] = input("Novo tipo: ")

            encontrado = True
            break

    if encontrado:
        with open("banco_dados.json", "w", encoding="utf-8") as arquivo:
            json.dump(objetos, arquivo, indent=4, ensure_ascii=False)

        print("\nObjeto atualizado com sucesso!")

    else:
        print("\nObjeto não encontrado.")