# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

menor = a

if b>a and b>c:
    menor = b
if c<a and c<b:
    menor = c

maior = c

if c>a and c>b:
    maior = c

if b>a and b>c:
    maior = b


print('O menor número é {}'.format(menor))
print('O maior número é {}'.format(maior))
