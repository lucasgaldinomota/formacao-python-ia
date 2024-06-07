class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa("Bia", 34)
p1.nome = "Pedro"
print(p1.nome, p1.idade)

p2 = Pessoa("Ana", 29)
print(p2.nome, p2.idade)
