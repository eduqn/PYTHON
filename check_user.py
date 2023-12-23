#Programa: Check de user e password
#Autor: Eduardo Nascimento
#Data: 21/12/2023

user = "a"
password = "123"
print("***** PROGRAMA LOGIN *****")
user1 = input("Digite o user: ")
print(f"User digitada foi {user1} ")
password1 = input("Digite o password: ")
print(f"Password digitada foi {password1} ")

print("*********************************\n")
if user1 == user and password1 == password:
    print("User e password CORRETOS!")
elif user1 != user and password1 != password:
    print("User e password INCORRETOS!")
elif user1 != user:
    print("User INCORRETO!")
else:
    print("Password INCORRETO!")
