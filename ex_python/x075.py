# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

lista = int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')),\
        int(input('Digite o terceiro número: ')), int(input('Digite o quarto número: '))

print(lista)
print(f'O valor 9 foi digitado {lista.count(9)} X.')
if 3 in lista:
    print(f'O valor 3 esta na posição {lista.index(3)}.')
else:
    print('O número 3 não foi digitado!')
print('Os números pares digitados foram: ', end="")
for n in lista:
    if n % 2 == 0:
        print(n, end=' ')

