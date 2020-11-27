#galera = [['Joaquim', 30], ['Pedro', 28], ['Miguel', 18]]
#print(galera[2][0])
dado = []
galera = []
totalmai = totalmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
#print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade com {p[1]} anos')
        totalmai += 1
    else:
        print(f'{p[0]} é menor de idade com {p[1]}')
        totalmen += 1
print(f'Temos {totalmai} maiores de idade e {totalmen} menores de idade ')