from datetime import date
anoatual = date.today().year
contmaior = 0
contmenor = 0
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c} pessoa nasceu: '))
    if anoatual - ano >= 21:
        contmaior += 1
    else:
        contmenor += 1
print(f'Ao todo tiveram {contmaior} pessoas maiores de idade')
print(f'E tambem tivemos {contmenor} pessoas menores de idade')