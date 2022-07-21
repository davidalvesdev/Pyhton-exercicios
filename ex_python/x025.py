#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA”

nome = str(input('digite um nome:')).strip()

print('o nome tem silva?:{}'.format('silva'in nome.lower()))