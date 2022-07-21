#Escreva um programa que faça o computador “pensar” em um número inteiro
#entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep

computador = randint(0, 5) #computador faz uma escolha entre o intervalo de numeros

pessoa = int(input('Digite um número de 0 à 5: '))

print('numero escolhido {}'.format(computador))
sleep(3) #faz o computador paralizar pelo tempo determinado
if computador == pessoa:
    print('Você foi o ganhador!')
else:
     print('Você perdeu!')

