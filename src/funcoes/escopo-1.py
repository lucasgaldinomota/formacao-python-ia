def exibir_nome():
    # Escopo Local
    nome_completo = f"Pedro {sobrenome}"
    print(nome_completo)


# Escopo Global
sobrenome = 'Silva'

exibir_nome()
# print(nome_completo)
