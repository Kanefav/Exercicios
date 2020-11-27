from random import randint
print('-='*14)
print('Vamos Jogar Par ou Ímpar')
print('-='*14)
cont = 0
while True:
    computador = randint(1, 20)
    jogador = int(input('Digite um número: '))
    poui = str(input('Par ou Ímpar: ')).upper().strip()[0]
    soma = computador + jogador
    if soma % 2 == 0:
        print(f'Voçe jogou {jogador} e o computador {computador}. Total deu {soma} deu Par')
        if poui == 'P':
            print('Voçe Venceu')
            print('Vamos jogar novamente')
            cont += 1
        else:
            print('VOÇE PERDEU!')
            break
    else:
        print(f'Voçe jogou {jogador} e o computador {computador}. Total {soma} deu Ímpar')
        if poui == 'P':
            print('VOÇE PERDEU!')
            break
        else:
            print('Voçe Venceu')
            print('Vamos jogar novamente')
            cont += 1
print(f'GAME OVER! Voçe Venceu {cont} vezes')