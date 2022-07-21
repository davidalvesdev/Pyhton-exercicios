# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes


print('-=' * 20)
print('Analisador de triangulo')
print('-=' * 20)

r1 = float(input('Primeiro número: '))
r2 = float(input('Segundo número: '))
r3 = float(input('Terceiro número: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar um triangulo ', end='')
    if r1 == r2 == r3:
        print('EQUILATERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓCELES')
else:
    print('Os seguimentos acima não podem formar um triangulo')