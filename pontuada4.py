import os
os.system("cls")


print("""
Fruta   |	5 kg	            |Acima de 5 kg
________ _______________________ ______________
Morango | R$ 2,50 por Kg	    |R$ 2,20 por Kg
Maçã    | R$ 1,80 por Kg	    |R$ 1,50 por Kg


""")

morango = float(input("quantos kg de morango "))
maça = float(input("quantos kg de maça "))




if morango and maça > 10:
    desconto = morango + maça / 10
else:
    valor = morango + maça

print(f"valor{desconto}")
