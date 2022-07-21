#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. Exemplos de palíndromos:

frase = str(input('Digite uma frase: ')).strip().upper()

palavra = frase.split()
junto = ''.join(palavra)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)

if junto == inverso:
    print('É Palíndromo!')
else:
    print('NÃO É Palíndromo!')