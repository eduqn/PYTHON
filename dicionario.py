#Programa: Dicionário com dados
#Autor: Eduardo Nascimento
#Data: 28/12/2023

dados = {'nome': 'Mauhdbuk', 'idade': '34', 'cidade': 'Orlando'}
print(dados)
print(f'{'Nome'.ljust(20)} | {'Idade'.ljust(10)} | {'Cidade'}')
nome = dados['nome']
idade = dados['idade']
cidade = dados['cidade']
print(f'{nome.ljust(20)} | {idade.ljust(10)} | {cidade.ljust(10)}')

#update dado idade
i = {'idade': '18'}
dados.update(i)
idade = dados['idade']
print(f'{nome.ljust(20)} | {idade.ljust(10)} | {cidade.ljust(10)}')
print (dados)

#add dado profissão
dados['profissão'] = 'Eletrônico'
profissão = dados['profissão']        
print(f'{nome.ljust(20)} | {idade.ljust(10)} | {cidade.ljust(10)} | {profissão}')
print (dados)

#del dado cidade
del dados['cidade']
print(f'{nome.ljust(20)} | {idade.ljust(10)} | {cidade.ljust(10)} | {profissão}')
print (dados)




