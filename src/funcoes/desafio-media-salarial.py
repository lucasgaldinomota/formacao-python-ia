def obter_cargos():
    resposta = ""
    cargos = []

    while resposta.lower() != "n":
        cargo = input("Informe o cargo: ")
        qtde = int(input("Informe a qtde: "))
        salario = float(input("Informe o salário: "))

        cargos.append({
            "cargo": cargo,
            "qtde": qtde,
            "salario": salario,
        })

        resposta = input("Deseja continuar? (S/n): ")

    return cargos


def media_salarial(cargos):
    total_salarial = 0
    qtde_funcionarios = 0

    for cargo in cargos:
        total_salarial += cargo["qtde"] * cargo["salario"]
        qtde_funcionarios += cargo["qtde"]

    return total_salarial / qtde_funcionarios


cargos = obter_cargos()
media = media_salarial(cargos)
print(f"A média salarial é R$ {media:.2f}")
