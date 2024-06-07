class FuncionarioV1:
    def __init__(self, salario):
        self.__salario = salario

    # GETTER
    def get_salario(self):
        return self.__salario

    # SETTER
    def set_salario(self, novo_salario):
        self.salario = novo_salario

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo_salario):
        if novo_salario <= 1300:
            raise ValueError(
                "O salário não pode ser menor que o salário mínimo.")
        self.__salario = novo_salario


func = FuncionarioV1(1300)
# func.__salario = 2000
print(func.get_salario())

print(func.salario)

func.salario = 1500
func.set_salario(1980)
print(func.salario)
