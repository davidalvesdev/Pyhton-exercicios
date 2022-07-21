#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

km = float(input('Digite a distancia da viagem em km: '))

if km <= 200:
    preço = km * 0.5
else:
    preço = km * 0.45

print(" A sua viagem é de {:.0f}km e custará {:.2f} reais".format(km, preço))

