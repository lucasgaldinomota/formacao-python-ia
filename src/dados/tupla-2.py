# Criando uma tupla
tupla = (1, 2, 3, 4, 5, 2, 2)

# Métodos disponíveis para as tuplas
print(tupla.count(2)) # Saída: 3
print(tupla.index(5)) # Saída: 4

print(len(tupla)) # Saída: 7
print(max(tupla)) # Saída: 5
print(min(tupla)) # Saída: 1
print(sorted(tupla)) # Saída: (1, 2, 2, 2, 3, 4, 5)
print(sum(tupla)) # Saída: 19
print(all(tupla)) # True se todos os elementos da tuplas forem verdadeiros
