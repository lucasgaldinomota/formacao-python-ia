numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in numeros:
    if n % 2 == 0:
        continue
    
    print(n, end=" ")

print("")

for n in numeros:
    if n == 5:
        break
    
    print(n, end=" ")

print("Fim!")
