#Programa: Classificação por idade
#Autor: Eduardo Nascimento
#Data: 21/12/2023

print("***** PROGRAMA FAIXA ETÁRIA *****")
idade = int(input("Qual sua idade? "))
print(f"A idade digitada foi {idade} ")

print("*********************************\n")
if 0 <= idade <=12:
    print("Você é CRIANÇA!")
elif 13 <= idade <= 18:
    print("Você é ADOLESCENTE!")
else:
    print("Você é ADULTO!")
