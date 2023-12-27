import os

restaurantes = ['Pizza', 'Sushi', 'Churrasco']

def exibir_nome_app():
    print("""
        ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
        ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
        ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
        ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
        ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
        ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
            
    1. Cadastrar Restaurante
    2. Listar Restaurante
    3. Ativar Restaurante
    4. Sair
    """)

def menu_opcao():        
    try:
        opcao = int (input("Digite a opção desejada: "))
        if opcao == 1:
            cadastrar_restaurante()
        elif opcao == 2:
            listar_restaurantes()
        elif opcao == 3:
            print("Ativar Restaurante")
        elif opcao == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def finalizar_app():
    os.system("cls")
    print ("Finalizando o programa...")

def opcao_invalida():
    print("Opçaõ inválida!")
    print("Digite qualquer tecla para voltar ao menu principal")
    main()

def cadastrar_restaurante():
    os.system("cls")
    print("*** CADASTRO DE RESTAURANTE ***")
    nome_do_restaurante = input("Digite o nome do restaurante: ")
    restaurantes.append(nome_do_restaurante)
    print(f"O Restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    input("Pressione qualquer tecla para sair...")
    main()

def listar_restaurantes():
    os.system('cls')
    print("*** LISTA DE RESTAURANTES ***")
    for restaurante in restaurantes:
        print(f'.{restaurante}')
    input("Pressione qualquer tecla para sair...")
    main()

def main():
    os.system("cls")
    exibir_nome_app()
    menu_opcao()

if __name__ == '__main__':
    main()