# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
# mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres
# têm menos de 20 anos.

somaidade = 0
maioridadehomem = 0
nomemaisvelho = ''
totmulher20 = 0
for p in range(1, 5):
 print('---- {}ª pessoa ----'.format(p))
 nome = str(input('NOME: ')).strip().upper()
 idade = int(input('IDADE: '))
 sexo = str(input('SEXO [M/F]: ')).strip().upper()
 somaidade += idade
 if p == 1 and sexo == 'M':
   maioridadehomem = idade
   nomemaisvelho = nome
 if sexo == 'M' and idade > maioridadehomem:
    maioridadehomem = idade
    nomemaisvelho = nome
 if sexo == 'F' and idade < 20:
  totmulher20 += 1

mediaidade = somaidade / 4

print('A media de idade do grupo é de {}'.format(mediaidade))
print('O nome do homem mais velho é {} com {} anos'.format(nomemaisvelho, maioridadehomem))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))



