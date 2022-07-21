salario = float(input('Qual salario do funcionario?'))

aumento = salario * 0.15

print("Um funcionario que ganhava R${}, com 15% de aumento, passa a ganha R${:.2f}".format(salario, (salario + aumento)))