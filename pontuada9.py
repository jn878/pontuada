import os
os.system("cls")

renda = float(input("qual valor da rensa mensal"))
valor_emprestimo = float(input("qual valor do emprestimo"))
prestacoes = float(input("quantas parcelas serão divididas"))
valor_prestacao = float(input("qual valor das parcelas"))

criterio_emprestimo = valor_emprestimo * 10 >= renda and (valor_prestacao * 0.30) - renda


if valor_emprestimo >= criterio_emprestimo:
    print("emprestito concedido com sucesso")
else:
    print("emprestimo não concedido")