# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resp = 'S'
soma = cont = media = maior = menor = 0

while resp in 'S':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Deseja continuar digitando? ')).strip().upper()

media = soma/cont
print('A media dos valores é {}'.format(media))
print('O maior número é {}'.format(maior))
print('O menor numero é {}'.format(menor))
print('Acabou!')
