import os
os.system("cls")


valor1 = float(input("digite o valor "))
valor2 = float(input("digite o valor "))


if valor1 == valor2:
    resultado = valor1 + valor2
else:
    resultado = valor1 * valor2

print(f"resultado 1 {resultado}")
print("fim")
