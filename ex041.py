from datetime import date
ano = int(input('Ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - ano
print(f'O atleta tem {idade} anos')
if idade < 9:
    print('Classificação: MIRIM')
elif idade > 9 and idade <= 14 :
    print('Classificação: INFANTIL')
elif idade > 14 and idade <= 19:
    print('Classificação: JUNIOR')
elif idade > 19 and idade >= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classficação: MASTER')