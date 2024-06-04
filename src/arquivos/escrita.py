import os

pasta_atual = os.path.dirname(__file__)
caminho_arquivo = os.path.join(
    pasta_atual, 'textos', 'texto-01.txt'
)

with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write("Olá! Estou criando um arquivo com o Python!")

linhas = [
    "Escrevendo multiplas linhas",
    "em um arquivo de texto",
    "com Python",
]

with open(caminho_arquivo, 'a') as arquivo:
    arquivo.writelines("\n" + linha for linha in linhas)
