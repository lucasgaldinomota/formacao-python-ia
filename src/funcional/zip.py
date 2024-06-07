lista_nomes = ["Ana", "Pedro", "Maria", "João", "Rebeca"]
lista_idades = [23, 48, 32, 39, 27]
lista_estados = ['SP', 'CE', 'RJ', 'RS', 'MG']

resultado = zip(lista_nomes, lista_idades, lista_estados)
# print(dict(resultado))
# print(list(resultado))

for nome, idade, estado in resultado:
    print(f"{nome} tem {idade} anos e mora em {estado}")
