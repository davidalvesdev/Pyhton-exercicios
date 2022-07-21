# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C)  Uma listagem com as pessoas mais leves.

pessoas = list()
dado = []
maior = menor = 0
r = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    pessoas.append(dado[:])
    dado.clear()

    r = str(input('Deseja continuar[S/N]? '))
    if r in 'nN':
       break
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'o MAIOR peso foi  {maior}. Nome:', end='')
for p in pessoas:
    if p[1] == maior:
        print(f' {p[0]}', end='')
print()
print(f'o MENOR peso foi  {menor}. Nome: ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]} ', end='')