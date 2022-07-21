# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

valores = list()
cinco = 0
while True:
    valores.append(int(input('Digite um número: ')))
    r = str(input('Deseja continuar digitando [S/N]? '))
    if r in 'nN':
        break
valores.sort(reverse=True)
print(f'Foram digitados {len(valores)} números')
print(f'A lista ordenada: {valores}')
if 5 in valores:
    print('O 5 foi digitado na lista.')
else:
    print('O cinco não foi digitado na lista.')
