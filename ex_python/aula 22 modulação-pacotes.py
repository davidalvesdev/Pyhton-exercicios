#import uteis   # CRIA PRIMEIRO UM PYTHON FILE COM AS DEF E DEPOIS IMPORTA E UTILIZA DA MANEIRA ABAIXO

from uteis import números # AQUI ELE ESTA BUSCANDO DE DENTRO DE UM PACOTE

num = int(input('Digite um valor: '))
fat = números.fatorial(num)                    # AQUI
print(f'O fatorioal de {num} é {fat}')
print(f'O dobro de {num} é {números.dobro(num)}')    # AQUI


# PACOTE PYTHON SERVE PARA ARMAZENAR MODULOS POR TIPOS QUANDO AS QUANTIDADES DE MODULOS FOREM GRANDES
# PARA CRIAR UM PACOTE VAI NA PASTA -> NEW -> PYTHON.PACKAGE