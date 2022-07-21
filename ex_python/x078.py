# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
# mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = []
maior = 0
menor = 0
#for c in range(0, 5):                                 # simplificado começa aqui
#    valores.append(int(input('Digite um valor: ')))

#print(f'O maior valor digitado foi {max(valores)}!')
#print(f'O menor valor digitado foi {min(valores)}!')  # simplificado termina aqui

for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]

print(f'O maior valor digita foi {maior}! na posição: ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print('')
print(f'O menor valor digitado foi {menor} na posição: ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')

# ABAIXO A MANEIRA DE VERIFICAR AS PRIMEIRAS POSIÇÕES DE MAIOR E MENOR

#valores = []
#for c in range(0, 5):
#    valores.append(int(input('Digite um valor: ')))

#maior = max(valores)
#menor = min(valores)

#print(valores.index(menor))

#print(f'O maior valor digitado foi {max(valores)} na posição {valores.index(maior)}!')
#print(f'O menor valor digitado foi {min(valores)} na posição {valores.index(menor)}!')