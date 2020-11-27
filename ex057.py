sexo = str(input('Informe Seu Sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'mMfF':
    sexo = input('Dados Inválidos. Por Favor, Informe Seu Sexo: ').strip().upper()[0]
print(f'Sexo {sexo.upper()} Resgistrado')