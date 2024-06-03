import random


def gerar_aposta_mega(qtde=6):
    aposta = []

    if 6 <= qtde <= 20:
        aposta = random.sample(range(1, 61), qtde)
        aposta.sort()

    return aposta


print(gerar_aposta_mega())
print(gerar_aposta_mega(9))
print(gerar_aposta_mega(12))
print(gerar_aposta_mega(20))
