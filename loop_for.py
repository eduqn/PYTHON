#Programa: Listas em Python
#Autor: Eduardo Nascimento
#Data: 27/12/2023

numeros = [1,2,3,4,5,6,7,8,9,10]
somador = 0
for numero in numeros:
    resto = numero % 2
    if resto != 0: 
        somador += numero
print(f'Soma dos ímpares de 0 a 10 é: {somador}')
