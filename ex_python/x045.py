# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!')
print('Você escolheu {}'.format(itens[jogador]))
print('O computador escolheu {}'.format(itens[computador]))
if computador == 0: #pedra
    if jogador == 0:
        print('Empatou!')
    elif jogador == 1:
        print('Você ganhou!')
    elif jogador == 2:
        print('O computador ganhou!')
elif computador == 1: #papel
    if jogador == 0:
        print('O computador ganhou!')
    elif jogador == 1:
        print('Empatou!')
    elif jogador == 2:
        print('Você ganhou')
elif computador == 2: # tesoura
    if jogador == 0:
        print('Você ganhou!')
    elif jogador == 1:
        print('O computador ganhou!')
    elif jogador == 2:
        print('Empatou!')

