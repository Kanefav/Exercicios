dado = []
galera = []
pmaior = pmenor = 0
while True:
    galera.append(str(input('Nome: ')))
    galera.append(int(input('Idade: ')))
    if len(dado) == 0:
        pmaior = pmenor = galera[1]
    else:
        if galera[1] > pmaior:
            pmaior = galera[1]
        if galera[1] < pmenor:
            pmenor = galera[1]
    dado.append(galera[:])
    galera.clear()
    continuar = input('Quer continuar? [S/N] ').upper()
    if continuar == 'N':
        break
    else:
        continue
print(f'Ao todo, Você cadastrou {len(dado)}')
print(f'O maior peso foi {pmaior}. Peso de', end=' ')
for p in dado:
    if p[1] == pmaior:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi {pmenor}. Peso de', end=' ')
for p in dado:
    if p[1] == pmenor:
        print(f'{p[0]} ', end='')
print()
