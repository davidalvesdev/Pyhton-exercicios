import math

angulo = float(input('Digite o angulo que deseja:'))

print('O angulo de {} tem SENO de {:.2f}'.format(angulo, math.sin(math.radians(angulo))))
print('O angulo de {} tem COSSENO de {:.2f}'.format(angulo, math.cos(math.radians(angulo))))
print('O angulo de {} tem TANGENTE de {:.2f}'.format(angulo, math.tan(math.radians(angulo))))
