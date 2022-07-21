# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

n = int(input('Digite o número: '))
for c in range(1, 11):
      print('{} X {:2} = {}'.format(n, c, n*c))