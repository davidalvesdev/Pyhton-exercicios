
#num = [2, 5, 9, 1, 7, 4]

#print(num)
#num.append(11) #adicionando ultimo lugar da lista
#print(num)


#num.sort()   # para ordenar
#num.sort(reverse=True) #ordenar de maneira reversa
#print(num)

#num.insert(2, 0) #adicionou o '0' na posição 2
#print(num)

#removendo elementos
#num.pop()   #remove o ultimo item da lista
#num.pop(2)   # aqui elimina o item na posição 2 na lista
#print(num)

#num.remove(2) # remove o 2 contado do inico da lista para o fim

#print(num)

#if 4 in num:
 #   num.remove(4)
#else:
 #   print('Não achei o numero 4')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

#for v in valores:
#    print(f'{v}...', end='')

# para adicionar valores a lista:
#for cont in range(0, 5):
#    valores.append(int(input('Digite um valor: ')))

#for c, v in enumerate(valores):
#    print(f'Na posição {c} encontrei o valor {v}')
#print('Cheguei ao final da lista')

#para copiar uma lista
a = [1,3,6,9]
b = a[:]  #assim criamos uma copia e não fazemos uma ligação entre as duas linhas
b[2] = 8
print(a, '\n', b)