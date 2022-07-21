# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação
# de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[31mEntrada de dados interronpida pelo usuario.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[31mEntrada de dados interronpida pelo usuario.\033[m')
            return 0
        else:
            return n
num = leiaInt('Digite um valor: ')
print(f'O valor digitado foi {num}')