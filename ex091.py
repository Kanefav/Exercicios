from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
ranking = {}
for c in range(1, 5):
    jogadores['Jogador'] = randint(1, 6)
    sleep(1)
    print(f'Jogador{c} tirou {jogadores["Jogador"]} no dado')
    ranking[f'Jogador{c}'] = jogadores['Jogador']
print('-='*24)
ranking = sorted(ranking.items(), key=itemgetter(1), reverse=True)
print('  -=-= Ranking dos jogadores -=-=')
for c, i in enumerate(ranking):
    print(f'{c+1}º lugar: {i[0]} com {i[1]}')