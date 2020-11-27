from random import randint
list = []
print('-'*16)
print('    JOGO NA MEGA SENA    ')
print('-'*16)
vezes = int(input('Quantos jogos quer que eu sorteie? '))
print(f'-=-= SORTEANDO {vezes} JOGOS -=-=')
for c in range(0, vezes):
    list.clear()
    for c in range (0, 6):
        list.append(randint(1, 60))
        set(list)
        list.sort()
    print(f'JOGO {c}: {list}')
print('-=-= BOA SORTE -=-=')