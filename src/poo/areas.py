class Areas:
    PI = 3.14

    @staticmethod
    def circulo(raio):
        return Areas.PI * raio ** 2

    @staticmethod
    def triangulo(base, altura):
        return (base * altura) / 2

    def retangulo(base, altura):
        return base * altura

    @classmethod
    def alterar_pi(cls, novo_pi):
        cls.PI = novo_pi


print(Areas.PI)
Areas.alterar_pi(3.1415)
print(Areas.circulo(2.5))
print(Areas.triangulo(6, 10))
print(Areas.retangulo(10, 10))
