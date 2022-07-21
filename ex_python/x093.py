# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = {}
partidas = []
total = 0
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for p in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {p+1}º? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for i, v in jogador.items():
    print(f'O campo {i} tem o valor {v} ')
print('-=' * 30)
print(f' O jogador {jogador["nome"]} jogou {tot} partidas')
for n, g in enumerate(partidas):
    print(f'Na partida {n + 1}, fez {g} gols.')