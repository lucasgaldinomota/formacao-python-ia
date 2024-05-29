menu = [
    "Menu:",
    "------------",
    "1. Opção A",
    "2. Opção B",
    "3. Sair"
]

opcao_selecionada = 0

while opcao_selecionada != 3:
    print("\n".join(menu))

    opcao_selecionada = int(input("Informe a opção: "))

    if opcao_selecionada == 1:
        nome = input("Informe o seu nome: ")
        print(f"O nome informado foi {nome}")

        input("Enter para continuar...")
    elif opcao_selecionada == 2:
        email = input("Informe o seu e-mail:")
        print(f"O e-mail informado foi {email}")

        input("Enter para continuar...")
    elif opcao_selecionada == 3:
        print("Tchauuuuu!!!!")

print("Fim")
