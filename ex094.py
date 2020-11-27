galera = []
pessoas = {}
soma = media = 0
while True:
    pessoas.clear()
    pessoas['Nome'] = str(input('Nome: '))
    while True:
        pessoas['Sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoas['Sexo'] in 'MF':
            break
        print('ERRO! Por favor digite apenas M ou F.')
    pessoas['Idade'] = int(input('Idade: '))
    soma += pessoas['Idade']
    galera.append(pessoas.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Por favor digite apenas S ou N.')
    if continuar == 'N':
        break
print('-='*26)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media}')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]}', end= ' ')
print('D) Lista das pessoas que estão acima de média:')
for p in galera:
    if p['Idade'] >= 21:
        print(f'   nome = {p["Nome"]}; sexo = {p["Sexo"]}; idade = {p["Idade"]}')
print('<< ENCERRADO >>')