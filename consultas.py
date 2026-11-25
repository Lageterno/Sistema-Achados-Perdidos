import json

def listar_objetos():
    with open("banco_dados.json", "r", encoding="utf-8") as arquivo:
        objetos = json.load(arquivo)

    print("\n=== OBJETOS CADASTRADOS ===")

    if len(objetos) == 0:
        print("Nenhum objeto cadastrado.")

    else:
        for objeto in objetos:
            print("--------------------------")
            print("Nome:", objeto["nome"])
            print("Categoria:", objeto["categoria"])
            print("Descrição:", objeto["descricao"])
            print("Local:", objeto["local"])
            print("Data:", objeto["data"])
            print("Tipo:", objeto["tipo"])