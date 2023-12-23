#Programa: Check do Quadrante
#Autor: Eduardo Nascimento
#Data: 22/12/2023

print("***** PROGRAMA CHECK QUADRANTE *****")
x = int(input("Digite o valor de x: "))
y = int(input("Digite o password: "))
print("***********************************\n")
print(f"Valores das coordenadas: ({x},{y})")
print("Resultado: ")
if x > 0 and y > 0:
    print("O ponto está no Q1")
elif x < 0 and y > 0:
    print("O ponto está no Q2")
elif x < 0 and y < 0:
    print("O ponto está no Q3")
elif x > 0 and y < 0:
    print("O ponto está no Q4")
else:
    print("O Ponto está no eixo ou origem")