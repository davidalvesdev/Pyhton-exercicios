#Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

idade = sexo = homens = maior18 = mulhermenos = resp = 0

while True:
    idade = int(input('Digite a idade: '))
    sexo = " "
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]

    if idade >= 18:
        maior18 +=1
    if sexo == 'M':
        homens +=1
    if sexo == 'F' and idade < 20:
        mulhermenos +=1

    resp = " "
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break


print(f'{maior18} pessoas são maiores de 18 anos.')
print(f'{homens} homens foram cadastrados.')
print(f'{mulhermenos} mulheres menores de 20 anos')





