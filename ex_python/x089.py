# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
# notas de cada aluno individualmente.

ficha = list()

while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = n1 + n2 / 2
    ficha.append([nome, [n1, n2], media])
    resp = str(input('Deseja continuar [S/N]? '))
    if resp in 'nN':
        break
print(f'{"Nº":<4}{"Nome":<10}{"Media":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
while True:
    opc = int(input('Qual aluno deseja saber a nota? '))
    if opc == 999:
        break
    if opc <= len(ficha) -1:
        print(f'As notas do aluno {ficha[opc][0]} são {ficha[opc][1]}!')