jogador = {'nome': '','gols': [], 'total': 0}
jogador['nome'] = str(input('Nome: ')).capitalize()
partidas = int(input(f'Quantas Partidas {jogador["nome"]} jogou? '))
for c in range(0, partidas):
    gols = int(input(f'Quantos gols na partida {c}: '))
    jogador['gols'].append(gols)
    jogador['total'] += gols
print('-='*24)
print(jogador)
print('-='*24)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*24)
print(f'O jogador {jogador} jogou {partidas}.')
for c in range(0, len(jogador['gols'])):
    print(f'    => Na partida {c}, fez {jogador["gols"][c]}.')
print(f'Foi um total de {jogador["total"]}')