print('Gerador de PA')
print('-=' *10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
cont2 = 10
while cont2 != 0:
    total += cont2
    while cont <= total:
        print(f'{termo} - ', end='')
        termo += razao
        cont += 1
    print('Pausa')
    cont2 = int(input('Quantos Termos Voçe que Mostrar a Mais: '))
print(f'Progressão Finalizada com {total} Termos Mostrados')