def divisao_inteira(a, b):
    quociente = a // b
    resto = a % b

    return quociente, resto


resultado = divisao_inteira(10, 3)
print(resultado)

(q, r) = divisao_inteira(20, 7)
print(q, r)
