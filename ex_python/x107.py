# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda
num = float(input('Digite um número: '))
print(f'A metade de {num} é {moeda.metade(num)}')
print(f'O dobro de {num} é {moeda.dobro(num)}')
print(f'Aumentando 10% temos {moeda.aumento(num):.1f}')