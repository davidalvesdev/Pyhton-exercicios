#Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
total = 0
acimamil = 0
cont = 0
menor = 0
barato = 0
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    total += preco
    cont +=1
    if preco >= 1000:
        acimamil +=1

    if cont == 1 or preco < menor:
        menor = preco
        barato = produto


    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar comprando [S/N] ? ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'O total da compra é de R${total}')
print(f'{acimamil} itens custam mais de R$1000.')
print(f'O item mais barato foi o {barato} e custa R${menor}!')