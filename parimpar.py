#Programa: Detecta se o número é PAR OU ÍMPAR
#Autor: Eduardo Nascimento
#Data: 21/12/2023

print("***** PROGRAMA PAR OU ÍMPAR *****")
numero = int(input("Entre com o número: "))
print(f"O número digitado foi {numero} ")
resto = numero % 2
print (resto)
print("*********************************\n")
if resto == 0:
    print("Número é PAR!")
else:
    print("Número é ÍMPAR!")