import os
os.system("cls")


nota1 = float(input("digite sua nota"))
nota2 = float(input("digite sua nota"))

media = nota1 + nota2 / 2

if media > 6:
    print("aprovado!")
elif media > 4.1 and media < 5.9:
    print("recuperação")
else:
    print("reprovado")
