# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
# Exercicio anterior:
# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
par = mai = somacoluna = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
     for c in range(0, 3):
         matriz[l][c] = int(input(f'Digite um valor para [{l}:{c}]: '))

for l in range(0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]

    print()

print(f'A soma de todos os valores pares é {par}!')
for l in range(0, 3):
    somacoluna += matriz[l][2]
print(f'A soma da terceira coluna é {somacoluna}!')
for c in range(0,3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz [1][c] > mai:
        mai = matriz[1][c]

print(f'O maior valor da segunda coluna é {mai}!')