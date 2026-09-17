import os
os.system("cls")


print("""
Fruta   |	5 kg	            |Acima de 5 kg
________ _______________________ ______________
Morango | R$ 2,50 por Kg	    |R$ 2,20 por Kg
Maçã    | R$ 1,80 por Kg	    |R$ 1,50 por Kg

kg_morango = float(input("Quantidade de morangos (Kg): "))
kg_maca = float(input("Quantidade de maçãs (Kg): "))

# Preço dos morangos
if kg_morango <= 5:
    preco_morango = kg_morango * 2.50
else:
    preco_morango = kg_morango * 2.20

# Preço das maçãs
if kg_maca <= 5:
    preco_maca = kg_maca * 1.80
else:
    preco_maca = kg_maca * 1.50

total_kg = kg_morango + kg_maca
total_preco = preco_morango + preco_maca

# Desconto de 10% se atingir 10 Kg no total ou passar de R$ 15,00
if total_kg >= 10 or total_preco > 15.00:
    total_preco *= 0.90

print(f"Valor a pagar: R$ {total_preco:.2f}")
