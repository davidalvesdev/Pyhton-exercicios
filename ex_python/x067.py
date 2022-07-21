# Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

n = int(input('Qual tabuada deseja visuaizar? '))
while True:
    if n > 0:
        for c in range(1, 11):
            resp = n * c
            print(f'{n:.0f} X {c:.0f} = {resp:.0f}')
    if n <= -1:
        break
    n = int(input('Qual tabuada deseja visuaizar? '))
print('Fim!')



