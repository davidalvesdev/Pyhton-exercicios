lanche = ('hamburguer', 'suco', 'pizza', 'pudim')

#maneiras de utlizar o for com tuplas

#for cont in range(0, len(lanche)):
 #   print('comi', lanche[cont])

#for comida in lanche:
 #   print('comi', comida)

#for pos, comida in enumerate(lanche):
 #   print(f'comi {pos} {comida}')

#for cont in range(0, len(lanche)):
 #   print(f'comi {cont} {lanche[cont]}')

#print(sorted(lanche)) # sorteia e mostra uma lista em nova ordem
#print(lanche)

a = 1, 4, 3, 4
b = 5, 6, 7, 8
c = a + b
#print(c.count(4)) #quantas vezes aparece o número 4

print(c)
#print(c.index(3)) #mostra em qual posição o 3 se encontra
print(c.index(4, 2)) # mostrando posição 4 a partir da 2 posição