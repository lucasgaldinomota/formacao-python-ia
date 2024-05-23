funcionario = {
    "nome": "João Pedro",
    "idade": 31,
    "cidade": "São Paulo",
    "ativo": True
}

funcionario["ativo"] = False
print(funcionario)

funcionario.update({
    "idade": 27,
    "ativo": True,
    "profissao": "Reporter"
})
print(funcionario)

cidade = funcionario.pop("cidade")
print(cidade)
print(funcionario)

funcionario.clear()
print(funcionario)
