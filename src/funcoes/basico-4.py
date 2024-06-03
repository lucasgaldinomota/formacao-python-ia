# Função COM parâmetros e COM retorno
def conta_com_gorjeta(valor_conta, percentual_gorjeta):
    valor_gorjeta = valor_conta * percentual_gorjeta
    return valor_conta + valor_gorjeta


print(conta_com_gorjeta(120, 0.1))

valor_total = conta_com_gorjeta(485, 0.08)
print(f"O valor final da conta é {valor_total}")
