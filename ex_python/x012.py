produto = float(input('Quanto custa o produto?'))

desconto = produto * 0.05

final = produto - desconto

print('O produto custava {}, na promoção com desconto de 5% vai custar {:.2f} reais'.format(produto, final))