# Escreva um programa para aprovar o empréstimo bancário para a compra de
# uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A
# prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valordacasa = float(input('Qual o valor da casa? '))
salariocomprador = float(input('Qual o seu salario? '))
anospagamento = float(input('Pretende pagar em quantos anos? '))

valormensalc = salariocomprador * 0.30


parcelas = anospagamento*12

valorparcela = valordacasa / parcelas

print('Para pagar uma casa de R${:.2f} em {:.0f} anos, a prestação será de R${:.2f}'.format(valordacasa, anospagamento, valorparcela))

if valorparcela >= valormensalc:
    print('Empréstimo NEGADO!')
else: print('Empréstimo APROVADO!')