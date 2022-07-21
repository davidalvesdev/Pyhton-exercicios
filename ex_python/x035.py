# Desenvolva um programa que leia o comprimento de três retas e diga ao
# usuário se elas podem ou não formar um triângulo.

print('-=' * 20)
print('Analisador de triangulo')
print('-=' * 20)

r1 = float(input('Primeiro número: '))
r2 = float(input('Segundo número: '))
r3 = float(input('Terceiro número: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:

    print('Os seguimentos acima podem formar um triangulo')
else:
    print('Os seguimentos acima não podem formar um triangulo')
