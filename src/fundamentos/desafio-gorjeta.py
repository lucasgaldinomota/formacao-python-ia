valor = float(input('Valor total (R$): '))
gorjeta = float(input('Percentual da gorjeta (0-100): '))

valor_gorjeta = valor * gorjeta / 100
valor_final = valor + valor_gorjeta

print(f'O valor final da conta é R${valor_final}')
