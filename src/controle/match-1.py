n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
operacao = input("Informe a operação [+ - * /]: ")

resultado = 0

match operacao:
    case "+":
        resultado = n1 + n2
    case "-":
        resultado = n1 - n2
    case "*" | "x":
        resultado = n1 * n2
    case "/":
        resultado = n1 / n2
    case _:
        print("Operação não encontrada")

print(f"O resultado é {resultado}")
