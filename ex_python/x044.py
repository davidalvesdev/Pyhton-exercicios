# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
# e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço normal
# – 3x ou mais no cartão: 20% de juros

print('='*20, 'Loja do David', '='*20)
compra = float(input('Digite o valor das compras: '))
avista = compra - compra * 0.10
cartao = compra - compra * 0.05
emduas = compra - compra / 2
parcelado = compra - compra * 0.20

print('[1] à vista dinheiro/cheque')
print('[2] à vista cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    print('Sua compra é de {:.2f} reais e vai custar {:.2f} reais no final.'.format(compra, avista))
elif opcao == 2:
    print('Sua compra é de {:.2f} reais e vai custar {:.2f} reais no final.'.format(compra, cartao))
elif opcao == 3:
    print('Sua compra é de {:.2f} reais e serão duas parcelas de {:.2f} reais no final.'.format(compra, emduas))
elif opcao == 4:
    print('Sua compra é de {:.2f} reais, parcelando em 3x ou mais, não tem desconto'.format(compra, parcelado))