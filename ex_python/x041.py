# A Confederação Nacional de Natação precisa de um programa que leia o
# ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER
import datetime
from datetime import date

nasc = float(input('Qual seu ano de nascimento? '))
idade = date.today().year - nasc
if idade <= 0:
    print('Você digitou um ano de nascimento não valido, tente novamente!')
elif idade <= 9:
    print('Você tem {:.0f} anos. Sua categoria é Mirim!'.format(idade))
elif idade <= 14:
    print('Você tem {:.0f} anos. Sua categoria é Infantil!'.format(idade))
elif idade <= 19:
    print('Voce tem {:.0f} anos. Sua categoria é Júnior!'.format(idade))
elif idade <= 25:
    print('Voce tem {:.0f} anos. Sua categoria é Sênior!'.format(idade))
elif idade > 25:
    print('Você tem {:.0f} anos. Sua categoria é Master!'.format(idade))
