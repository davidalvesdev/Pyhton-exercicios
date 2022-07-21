# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

listagem = 'lapis', 1.75, 'Caneta', 2.0, 'Estojo', 5.00, 'mochila', 100.00

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end="")
    else:
        print(f'R${listagem[pos]:>6.2f}')