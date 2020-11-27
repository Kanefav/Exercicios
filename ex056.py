nomehomen = ''
idadesoma = 0
muie = 0
menos20 = 0
maioridadehomen = 0
for c in range(1, 5):
    print(f'{c} Pessoa')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    idadesoma += idade
    if sexo == 'F' and idade <20:
        muie += 1
    if c == 1 and sexo == 'M':
        maioridadehomen = idade
        nomehomen = nome
    if sexo == 'M' and idade > maioridadehomen:
        maioridadehomen = idade
        nomehomen = nome
mediaidade = idadesoma / 4
print(f'A media da idade do grupo é {mediaidade:.1f}')
print(f'O Homen mais velho tem {maioridadehomen} e se chama {nomehomen}')
print(f'Ao todo são {muie} mulheres com menos de 20 anos')