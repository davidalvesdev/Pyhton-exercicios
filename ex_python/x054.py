# Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
maior = 0
menor = 0
atual = date.today().year
for pess in range(1, 8):
    nasc = float(input('Digite {}º ano de nascimento: '.format(pess)))
    idade = atual - nasc
    if idade >= 18:
        maior += 1
    else:
         menor += 1
print('Dos anos de nascimentos informados, {} são maiores de idade e {} são menores de idade.'.format(maior, menor))



