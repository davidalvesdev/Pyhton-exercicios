# Escreva um programa em Python que leia um número inteiro qualquer e peça
# para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para
# hexadecimal

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão')
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
escolha = int(input('Qual sua escolha? '))
if escolha == 1:
    print('O número binario de {} é {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('O número octal de {} é {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('O número hexadecimal de {} é {}'.format(num, hex(num)[2:]))

else:
    print('Opção invalida, tente novamente!')
