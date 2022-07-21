# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
# crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

numeros = []
pares = []
impares = []
while True:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    r = str(input('Deseja continuar digitando [S/N]? '))
    if r in 'Nn':
        break
numeros = pares + impares
numeros.sort()
print(f'todos da lista {numeros}')
print(f'Números pares da lista: {pares}')
print(f'Números impares da lista: {impares}')

#OU

#while True:
#    n = int(input('Digite um número: '))
#    r = str(input('Deseja continuar digitando [S/N]? '))
#    if r in 'Nn':
#        break
#for i, v in enumerate:
#    if v % 2 == 0:
#        pares.append(v)
#    elif v % 2 == 1:
#        impares.append(v)

#print(f'todos da lista {numeros}')
#print(f'Números pares da lista: {pares}')
#print(f'Números impares da lista: {impares}')
