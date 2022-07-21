# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opcao = 0

while opcao != 5:
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    opcao = int(input('Qual a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é o total de {}\n'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('A multiplicação entre {} e {} é o total de {}\n'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior número entre {} e {} é o {}\n'.format(n1, n2, maior))
    elif opcao == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opcao == 5:
        print('O programa esta finalizando...\n')
        sleep(2)
    else:
        print('Opção invalida, tente novamente!')
print('Fim do programa. ')
