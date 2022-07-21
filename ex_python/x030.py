# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Digite algum numero: '))

resultado = numero % 2  # o resto de divisão para qualquer numero impar é 1 e para qualquer numero par é 0
# quando multiplica inteiro por 2


if resultado == 0:
    print('Numero par')
else:
    print('Numero impar')
