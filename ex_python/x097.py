# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro
# e mostre uma mensagem com tamanho adaptável.
# Ex:
# escreva(‘Olá, Mundo!’)
# Saída:
# ~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~

def escreva(a):
    print('~' * 8)
    print(f'{a}')
    print('~' * 8)

a = 'Olá Mundo!'
escreva(a)


