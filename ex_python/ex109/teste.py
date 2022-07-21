# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import ex109

# programa principal
p = float(input('Digite o preço: R$'))
print(f'A metade de {ex109.moeda(p)} é {ex109.metade(p, True)}')
print(f'O dobro de {ex109.moeda(p)} é {ex109.dobro(p, True)}')
print(f'Aumentando 10%, temos {ex109.aumentar(p, 10, True)}')
print(f'Diminuindo 13%, temos {ex109.diminuir(p, 13, True)}')

def resumo(preco=0, taxa=10, taxa=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: {moeda(preco)}')
    print(f'Dobro do preço: {dobro(preco, True)}')
    print(f'Metade do preço: {metade(preco, True)}')
    print('-' * 30)
