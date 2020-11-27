from datetime import date
ano = int(input('Ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - ano
print(f'Quem nasceu em {ano} tem {idade} anos de idade em {anoatual}')
if idade == 18:
    print('Voçe tem que se alistar IMEDIATAMENTE')
elif idade > 18:
    anoalist = idade - 18
    alist = ano + 18
    print(f'Voçe ja deveria ter se alistado há {anoalist}')
    print(f'Seu alistamento foi em {alist}')
elif idade < 18:
    anoalist = 18 - idade
    alist = ano + 18
    print(f'Ainda faltam {anoalist} anos para o alistamento ')
    print(f'Seu alistamento será em {alist}')