import math

op = float(input('Digite o comprimento do cateto oposto:'))
ad = float(input('Digite o comprimento do cateto adjacente:'))

resultado = math.hypot(op, ad)

print('A hipotenusa vai medir {:.2f}'.format(resultado))