# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final,
# serão exibidos todos os valores únicos digitados, em ordem crescente.

numlista = list()

while True:
    n = int(input('Digite um número: '))
    if n not in numlista:
        numlista.append(n)
        print('Valor adicionado! ')
    else:
        print('Valor duplicado. Não vou adicionar!')
    r = str(input('Quer continuar? '))
    if r in 'Nn':
        break
print(numlista)



