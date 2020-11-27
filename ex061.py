print('Gerador de PA')
print('-=' *10)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    cont += 1
    print(f' {termo} ', end='')
    print('-'if cont < 11 else '=', end='')
    termo += razao #termo(primeiro) + primeiro
print(' Acabou')