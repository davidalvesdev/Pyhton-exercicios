
pessoas = {'nome':'Gustavo', 'sexo':'masculino'}
#print(pessoas['nome']) # VAI APARECER 'GUSTAVO'

#print(pessoas.keys()) # MOSTRA AS CHAVES
#print(pessoas.values()) # MOSTRA OS VALORES
#print(pessoas.items()) #M MOSTRA OS ITENS (TODOS OS JUNTOS)

#for k in pessoas.values(): # MUDANDO PARA FINAL VALUES TBM FAZ IGUAL
#    print(k)             # MOSTRA SOMENTE AS CHAVES

#for k, v in pessoas.items():   # EM ITENS FICA MELHOR DESSA FORMA
#    print(f'{k} = {v}')

    # PARA ADICIONAR EM DICIONARIOS É SÓ DECLARAR(INSERIR COMO SE JA TIVESSE), NÃO PRECISA USAR APPEND

#--------------------------------------------------------#

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Digite o estado: '))
    estado['sigla'] = str(input('Digite a sigla: '))
    brasil.append(estado.copy())                     # ADICIONANDO

print(estado)
#print(brasil)
# MOSTRANDO MELHOR
#for e in brasil:
#    print(e)

# MELHORANDO AINDA MAIS

#for e in brasil:
#    for k, v in e.items():         # PODE USAR e.valeues() e colocar somente o v em for
#        print(f'O campo {k} tem valor {v}')