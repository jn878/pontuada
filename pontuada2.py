import os
os.system("cls")


nome = input("digite seu nome: ")
sexo = input("digite seu sexo")
estado_civil = input("qual seu estado civil? ")

match sexo, estado_civil:
    case f,casada:
        input("quanto tempo de casamento? ")

print(f"nome informado: {nome}")
print(f"sexo informado: {sexo}")
print(f"estado civil informado: {estado_civil}")
