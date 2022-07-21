largura = float(input('Digite a largura:'))
altura = float(input('Digite a altura:'))

area = largura * altura

print('Sua parede tem a dimensao de {}x{} e sua area é de {}'.format(largura, altura, area))
print("Para pintar sua parede, você precisará de {} litros de tinta".format(area / 2))