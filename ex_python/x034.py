# Escreva um programa que pergunte o salário de um funcionário e calcule o
# valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os
# inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o seu salario: '))

# calculo para salarios superiores à 1.250

# calculo menor

if salario <= 1250:
    menor = salario * 0.15 + salario
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, menor))
else:
    maior = salario * 0.10 + salario
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, maior))
