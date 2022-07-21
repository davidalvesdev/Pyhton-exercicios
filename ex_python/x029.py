#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar
#80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada
#Km acima do limite.

velocidade = float(input('Velocidade em km: '))

if velocidade > 80:
    valormulta = (velocidade - 80) * 7
    print('Vc esta acima da velocidade permitida, sua multa é de {}'.format(valormulta))

print('tenha um bom dia e dirija com segurança!')