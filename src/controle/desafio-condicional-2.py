# Faça um programa que leia três números 
# e mostre qual é o maior e qual é o menor.
# Usar if - elif - else

n1 = int(input("Informe o número 1: "))
n2 = int(input("Informe o número 2: "))
n3 = int(input("Informe o número 3: "))

# Encontrar o MAIOR número
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
else:
    maior = n3

# Encontrar o MENOR número
if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
else:
    menor = n3


print(f"O maior valor é {maior}!")
print(f"O menor valor é {menor}!")
