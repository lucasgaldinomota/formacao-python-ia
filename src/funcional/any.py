lista = [1, 3, 5, 7, 9, 10]

r = any(n % 2 == 0 for n in lista)

if r:
    print("Pelo menos um número é par!")
else:
    print("Todos os números são ímpares!")
