#Programa: EXERCICIOS DE POO
#Autor: Eduardo Nascimento
#Data: 28/12/2023

class Restaurante():
    nome = 'empty'
    categoria = 'empty'
    ativo = False

restaurante_praca = Restaurante()

#1 atribuindo um valor a varialvel categoria do restaurante praca
restaurante_praca.categoria = 'Italiana'
restaurantes = [vars(restaurante_praca)]

#2 Acessando valor do atributo nome da instânica restaurante_praca da Classe Restaurante
nome_restaurante = restaurante_praca.nome 
print(nome_restaurante)

#3 Verificar o valor inicial do atributo ativo
ativo_restaurante = restaurante_praca.ativo
if ativo_restaurante:
    print(f'O restaurante está ativo: ', ativo_restaurante)
else:
    print(f'O restaurante está ativo: ', ativo_restaurante)

#4 Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
categoria = Restaurante.categoria
print(categoria)

#5 Altere o valor do atributo nome para 'Bistrô'.
restaurante_praca.nome = 'Bistrô'
print('Nome: ', restaurante_praca.nome)

#6 Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
print('Nome: ', restaurante_pizza.nome, ' | Categoria: ', restaurante_pizza.categoria)

#7 Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
if restaurante_pizza.categoria == 'Fast Food':
    print(f'O restaurante é: ', restaurante_pizza.categoria)
else:
    print(f'O restaurante NÃO é: ', restaurante_pizza.categoria)

#8 Mude o estado da instância restaurante_pizza para ativo.
restaurante_pizza.ativo = True
print('Estado do',restaurante_pizza.nome,'é',restaurante_pizza.ativo)

#9 Imprima no console o nome e a categoria da instância restaurante_praca.
print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')
