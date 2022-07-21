# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
# em uma lista única que mantenha separados os valores pares e ímpares. No final,
# mostre os valores pares e ímpares em ordem crescente.

todosnum = [[], []]
num = 0
for c in range(0, 7):
    num = int(input('Digite um valore: '))
    if num % 2 == 0:
        todosnum[0].append(num)
    else:
        todosnum[1].append(num)
print(f'Os valores pares são: {todosnum[0]}.')
print(f'Os valores impares são: {todosnum[1]}.')
