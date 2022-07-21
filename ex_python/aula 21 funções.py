def contador(i, f, p):
    """-> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
# tudo acima que foi escrito apos 3x " fica gravado na função e pode ser acessado utilizando help(contador)

#help(contador)


#def somar(a=0, b=0, c=0):    # AQUI COLOCANDO O =0 NO PARAMETRO ELE FICA OPCIONAL, PODE DIGITAR ATE A QUANTIDADE DE OPCIONAIS Q ESTIVER ESCRITA.
#    s = a + b + c
#    print(f'A soma vale {s}!')


#somar(2,5)
#somar(2,3,5)
#somar()

def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')         # n1 aqui funciona somente dentro da função então é n1 local

n1 = 2
funcao()
print(f'N1 fora vale {n1}')              # aqui o n1 é global e funciona em o programa

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f' Os valores {r1}, {r2} e {r3}.')