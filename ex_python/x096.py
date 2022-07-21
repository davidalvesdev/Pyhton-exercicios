# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def área(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno com a largura {largura} e comprimento  {comprimento} é {a}m²')


print('Controle de terrenos')
print('-=-' * 20)
largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))
área(largura, comprimento)
