def metade(n):
    return n / 2

def dobro(n):
    return n * 2

def aumento(n):
    return n * 0.10 + n

def real(n):
    return f'R${n:.2f}'

def diminuir(n):
    taxa = n * 0.13
    return n - taxa


#############################
modo que o guanabara fez

def resumo(preco=0, taxa=10, taxa=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: {moeda(preco)}')
    print(f'Dobro do preço: {dobro(preco, True)}')
    print(f'Metade do preço: {metade(preco, True)}')
    print('-' * 30)


from ex109 import moeda

# programa principal
p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos{moeda.aumentar(p, 10)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(p, 13)}')