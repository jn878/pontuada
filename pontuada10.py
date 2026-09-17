import os
os.system("cls")


tipo = input("Tipo (A - Álcool / G - Gasolina): ").upper()
litros = float(input("Quantidade de litros: "))


if tipo == "A":
    if litros <= 20:
        total = litros * (3.50 * 0.97)  # 3% de desconto
    else:
        total = litros * (3.50 * 0.95)  # 5% de desconto


else:
    if litros <= 20:
        total = litros * (4.60 * 0.96)  # 4% de desconto
    else:
        total = litros * (4.60 * 0.94)  # 6% de desconto

print(f"Total a pagar: R$ {total:.2f}")
