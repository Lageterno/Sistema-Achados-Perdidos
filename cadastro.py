import json

def cadastrar_objeto():
    print("\n=== CADASTRO DE OBJETO ===")

    nome = input("Nome do objeto: ")
    categoria = input("Categoria: ")
    descricao = input("Descrição: ")
    local = input("Local onde foi perdido/encontrado: ")
    data = input("Data: ")
    tipo = input("O objeto foi perdido ou encontrado? ")

    objeto = {
        "nome": nome,
        "categoria": categoria,
        "descricao": descricao,
        "local": local,
        "data": data,
        "tipo": tipo
    }

    with open("banco_dados.json", "r", encoding="utf-8") as arquivo:
        objetos = json.load(arquivo)

    objetos.append(objeto)

    with open("banco_dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(objetos, arquivo, indent=4, ensure_ascii=False)

    print("\nObjeto cadastrado e salvo com sucesso!")