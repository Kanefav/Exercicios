conthomens = contmulheres = contmais18 = 0
while True:
    print('-'*15)
    print('CADASTRE UMA PESSOA')
    print('-'*15)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]')).upper().strip()[0]
    print('-'*15)
    continuar = str(input('Quer Continuar: [S/N]')).upper().strip()[0]
    if idade >= 18:
        contmais18 += 1
    if sexo == 'M':
        conthomens += 1
    if sexo == 'F' and idade <= 19:
        contmulheres += 1
    if continuar == 'S':
        continue
    else:
        break
print(f'Total de pessoas com mais de 18 anos: {contmais18}')
print(f'Ao todo temos {conthomens} homens cadastrados')
print(f'E temos {contmulheres} mulheres com menos de 20 anos')