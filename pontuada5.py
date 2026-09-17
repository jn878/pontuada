import os
os.system("cls")


numero1 = float(input("digite o numero: "))
numero2 = float(input("digite o numero: "))
operação = input("digite a operação: ")

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

match operação:
    case "+":
        print(f"resultado {soma}")
    case "-":
        print(f"resultado {subtracao}")
    case "*":
        print(f"resultado {multiplicacao}")
    case "/":
        (f"resultado {divisao}")

