class Animal:
    def __init__(self, nome):
        self.nome = nome
        pass

    def expressar(self):
        return f"O {self.nome} está fazendo um som"


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def expressar(self):
        return f"{super().expressar()}... au au au"


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)


a1 = Animal("Animal")
print(a1.expressar())

a1 = Cachorro("Rex")
print(a1.expressar())

a1 = Gato("Mel")
print(a1.expressar())
