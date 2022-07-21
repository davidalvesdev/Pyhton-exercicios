# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ('Corinthias', 'Palmeiras', 'Santos', 'Gremio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atletico', 'Botafogo', 'Atletico PR', 'Bahia',
         'São paulo', 'Fluminense', 'Sport Recife', 'Ec Vitoria',
         'Coritiba', 'Avai', 'ponte preta', 'Atletico GO')

print(f'Os 5 primeiros times são {times[:5]}')
print(f'Os 4 ultimos colocados são {times[-4:]}')
print(f'Os times em ordem alfabetica são {sorted(times)}')
print(f'O Chapecoense esta na posição {times.index("Chapecoense") +1} posição!')
