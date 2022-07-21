# Crie um programa que leia o nome de uma pessoa e mostre:
# O nome com todas as letras maiusculas
# O nome com todas as letras minusculas
# Quantas letras tem o nome
# Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome:'))
print('seu primeiro nome em maiusculas: {}'.format(nome.upper()))
print('seu segundo nome em minusculas: {}'.format(nome.lower()))
print('seu nome tem {} letras'.format(len(nome) - (nome.count(' '))))

separa = nome.split()

print('seu primeiro nome tem {} letras'.format(len(separa[0])))
