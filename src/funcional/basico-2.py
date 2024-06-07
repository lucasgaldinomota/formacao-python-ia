def somar(a):
    def finalizar_soma(b):
        return a + b
    return finalizar_soma


print(somar(3)(4))

SALARIO_BASE = 2113.88
somar_com_salario_base = somar(SALARIO_BASE)

print(somar_com_salario_base(326.12))
print(somar_com_salario_base(444.12))
