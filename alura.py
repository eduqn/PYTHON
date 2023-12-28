import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo':False},
                {'nome': 'Pizza Suprema', 'categoria': 'Italian', 'ativo':True}, 
                {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo':False}
]

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
            alterar_estado_restaurante()
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
    print(f'{'Nome do Restaurante'.ljust(22)} || {'Categoria'.ljust(20)} || {'Status'}')
    for restaurante in restaurantes:
        nome_do_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo_restaurante = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_do_restaurante.ljust(20)} || {categoria.ljust(20)} || {ativo_restaurante}')
    input("Pressione qualquer tecla para sair...")
    main()

def alterar_estado_restaurante():
    print('*** Alterando estado do restaurante ***')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado!') 


    
    input("Pressione qualquer tecla para sair...")
    main()

def main():
    os.system("cls")
    exibir_nome_app()
    menu_opcao()

if __name__ == '__main__':
    main()