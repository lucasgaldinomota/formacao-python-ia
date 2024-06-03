def calcular_media(*numeros):
    return sum(numeros) / len(numeros)


media = calcular_media(7, 8, 7.5, 9, 8.8, 4.9, 7.7)
print(f"O valor da média é {media:.1f}")
