import os
os.system("cls")

nome = input("digite o nome do produto ")
quantidade = int(input("digite a quantidade "))
preco = float(input("preço unitario "))



if quantidade <=5:
    desconto = preco / 0.2
elif quantidade > 5 and quantidade <=10:
    desconto = preco / 0.3
elif quantidade > 10:
    desconto = preco / 0.5

preco_final = desconto - preco
sem_desconto = preco * quantidade

print(f"\ntotal sem desconto {sem_desconto}")
print(f"\nnome {nome}")
print(f"\nquantidade  {quantidade}")
print(f"\ndesconto {desconto}")
print(f"\ntotal {preco_final}")
