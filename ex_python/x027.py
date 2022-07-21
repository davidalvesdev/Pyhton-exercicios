#Faça um programa que leia o nome completo de uma pessoa, mostrando em
#seguida o primeiro e o último nome separadamente.

frase = str(input("Digite seu nome:")).strip()
print("muito prazer!")
nome = frase.split()

print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))