nome = """
Pedro de Alcântara João Carlos Leopoldo
Salvador Bibiano Francisco Xavier de Paula
Leocádio Miguel Gabriel Rafael Gonzaga
de Bragança e Habsburgo
"""

partes_nome = nome.split()

match partes_nome:
    case [primeiro]:
        sigla = primeiro[0:2]
    # case [primeiro, segundo]:
    #     sigla = primeiro[0] + segundo[0]
    case [primeiro, *m, ultimo]:
        sigla = primeiro[0] + ultimo[0]
    case _:
        sigla = "AL"

print(f"A sigla do usuário é {sigla.upper()}")
