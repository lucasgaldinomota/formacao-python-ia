import os


def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def exibir_menu():
    limpar_terminal()

    print("Menu:")
    print("---------------")
    print("1. Opção A")
    print("2. Opção B")
    print("3. Sair")


def opcao_a():
    limpar_terminal()
    
    nome = input("Informe o seu nome: ")
    print(f"O nome informado é {nome[::-1]}")
    
    input("Digite ENTER para continuar...")


def opcao_b():
    limpar_terminal()
    
    email = input("Informe o seu e-mail: ")
    dominio = email.split('@')[1]
    print(f"O domínio do email é {dominio}")
    
    input("Digite ENTER para continuar...")


def main():
    opcao_selecionada = 0

    while opcao_selecionada != 3:
        exibir_menu()
        opcao_selecionada = int(input("Selecione [1-3]: "))

        match opcao_selecionada:
            case 1: opcao_a()
            case 2: opcao_b()


main()
