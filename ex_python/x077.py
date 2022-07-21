# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavra = 'abacate', 'melancia', 'tomate', 'limao', 'abacaxi'

for p in palavra:
    print(f'\nNa palavra {p} tem: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end='')
