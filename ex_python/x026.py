#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes
#aparece a letra “A”, em que posição ela aparece a primeira vez e em que
#posição ela aparece a última vez.

frase = str(input('Digite uma frase:')).lower()

print('A letra "a" aparece {} vezes.'.format(frase.count('a')))
print('A letra "a" aparece pela primeira vez na posição {}'.format(frase.find('a')+1))
print('A letra "a" aparece pela ultima vez na posição {}'.format(frase.rfind('a')+1))