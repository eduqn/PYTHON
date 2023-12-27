#Programa: Soma de valores de uma lista
#Autor: Eduardo Nascimento
#Data: 27/12/2023

lista_numeros = [5, 3, 18]
soma = 0
soma1 = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

try:
    for valor in lista_numeros:
        soma1 += valor
    print(f"Média dos elementos: {soma1 / len(lista_numeros)}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
