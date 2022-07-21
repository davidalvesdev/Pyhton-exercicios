# LISTAS COMPOSTAS

#pessoas= [['Pedro', 25], ['Maria', 19], ['João', 32]]
#              0                1            2

#print(pessoas[1][1])  # 19
#print(pessoas[0][0])   # PEDRO
#print(pessoas[2][0])   # JOAO
#print(pessoas[1])      # ['Maria', 19]

#teste = list()
#teste.append('Gustavo')
#teste.append(40)
#galera = list()
#galera.append(teste[:])
#teste[0] = 'Maria'
#teste[1] = 22
#galera.append(teste[:])

#print(galera)

# MOSTRANDO SOMENTE NOME

#galera = [['João', 45 ], ['Maria', 26], ['Daniel', 23], ['Joana', 21]]
#print(galera) # MOSTRA LISTA INTEIRA

#for p in galera:
#    print(f'O {p[0]} tem {p[1]} de idade')  # AQUI MOSTRA O NOME E IDADE DA LISTA.

#galera = []
#dado = []
#for c in range(0, 3):
#    dado.append(str(input('Nome: ')))
#    dado.append(int(input('Idade: ')))
#    galera.append(dado[:])
#    dado.clear()
#print(galera)

#for p in galera:
#    if p[1] > 18:
#        print(f'O {p[0]} tem {p[1]}, portanto é MAIOR de idade') #  SENDO MAIOR DE 18
#    else:
#        print(f'O {p[0]} tem {p[1]}, portando é MENOR de idade') # SENDO MENOR DE 18