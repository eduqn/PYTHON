#Programa: Métodos especiais e atributos
#Autor: Eduardo Nascimento
#Data: 28/12/2023

#1 Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro:
     
    def __init__(self, modelo = '', cor = '', ano = 0):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

carro1 = Carro(modelo='Uno', cor='Prata', ano=1998)
print (f'{carro1.modelo} | {carro1.cor} | {carro1.ano}')

#2 Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.

class Restaurante:
    def __init__(self, nome='', categoria='', endereco='', ano=0, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.endereco = endereco
        self.ano = ano
        self.ativo = ativo

restaurante1 = Restaurante(nome='Splash Pizzaria', categoria='Italiana', endereco='D. Pedro', ano=2000)
print (f'{restaurante1.nome} | {restaurante1.categoria} | {restaurante1.endereco} | {restaurante1.ano}')