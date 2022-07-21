from ex115.lib.interface import *
from ex115.lib.arquivo import *

from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # OPÇÃO DE LISTAR O CONTEUDO DE UM ARQUIVO
        lerArquivo(arq)
    elif resposta == 2:
        # OPÇÃO CADASTRAR NOVA PESSOA
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[33mERRO! Digite uma opção valida!\033[m')
    sleep(2)




