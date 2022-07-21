# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# entre 4 e 6 recuperação
# entre 7 e 10 aprovado
# entre 0 e 3 reprovado

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media >= 7:
    print('Sua nota foi {:.2f}, você foi APROVADO!'.format(media))
elif media >= 4 <= 6:
   print('Sua nota foi {:.2f}, você esta de RECUPERAÇÃO'.format(media))
elif media <= 3:
   print('Sua nota foi {:.2f}, você foi REPROVADO'.format(media))