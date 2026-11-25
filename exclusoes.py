import json

def excluir_objeto():
    with open("banco_dados.json", "r", encoding="utf-8") as arquivo:
        objetos = json.load(arquivo)

    print("\n=== EXCLUIR OBJETO ===")

    nome_busca = input("Digite o nome do objeto que deseja excluir: ")

    encontrado = False

    for objeto in objetos:
        if objeto["nome"].lower() == nome_busca.lower():

            print("\nObjeto encontrado!")
            print("Nome:", objeto["nome"])
            print("Local:", objeto["local"])

            confirmar = input("\nDeseja realmente excluir? (s/n): ")

            if confirmar.lower() == "s":
                objetos.remove(objeto)
                encontrado = True
                print("\nObjeto excluído com sucesso!")

            else:
                encontrado = True
                print("\nExclusão cancelada!")

            break

    if not encontrado:
        print("\nObjeto não encontrado.")

    else:
        with open("banco_dados.json", "w", encoding="utf-8") as arquivo:
            json.dump(objetos, arquivo, indent=4, ensure_ascii=False)