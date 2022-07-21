
#try:
#    a = int(input('Numerador: '))
#    b = int(input('Denominador: '))
#    r = a / b
#except Exception as erro:                              # UM MESMO TRY PODE TER VARIOS ESCEPTION
#    print(f'O erro encontrado foi {erro.__class__}')
#else:                                            # finally e else são opcionais
#    print(f'O resultado é {r:.1f}')

#finally:
#    print('Volte sempre! muito Obrigado!')


###############################

# ou assim

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero.')
except KeyboardInterrupt:
    print('O usuario preferio não informar os dados.')