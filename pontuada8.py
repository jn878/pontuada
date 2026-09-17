import os
os.system("cls")

cor = input("digite a cor")


match cor.strip().lower():
    case "verde":
        print("verde = 10,00 $")
    case "azul":
        print("azul = 20,00 $")
    case "amarelo":
        print("amarelo = 30,00 $")
    case "vermelho":
        print("vermelho = 40,00 $")
    case "":
        print("voce nao digitou nada")
    case _:
        print("essa cor nao existe")