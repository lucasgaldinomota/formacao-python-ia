class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def __str__(self) -> str:
        return f"Cliente: {self.nome}, {self.email}"


lista_clientes = [
    Cliente("João", "joao@empresa.com.br"),
    Cliente("Maria", "maria@gmail.com"),
    Cliente("Pedro", "pedro@empresa.com.br"),
    Cliente("Ana", "ana@yahoo.com"),
]

r1 = filter(lambda c: "@empresa.com.br" in c.email, lista_clientes)
clientes_filtrados = list(r1)

for cliente in clientes_filtrados:
    print(cliente)
