#km é 0.15
#dia alugado é R$60

dias = float(input('Quantos dias alugado?'))
km = float(input('Quantos Km rodados?'))

valordias = dias * 60
valorkm = km * 0.15

print('O total a pagar é de R${:.2f}!'.format(valordias + valorkm))