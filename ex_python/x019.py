import random

n1 = input('Digite o primeiro nome:')
n2 = input('Digite o segundo nome:')
n3 = input('Digite o terceiro número:')
n4 = input('Digite o quarto numero:')

lista = [n1, n2, n3, n4]


print('O aluno escolhido é {}'.format(random.choice(lista)))