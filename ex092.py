from datetime import datetime
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
pessoa['idade'] = datetime.now().year - nascimento
pessoa['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if pessoa['ctps'] > 0:
    pessoa['contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: '))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratacao'] + 35) - datetime.now().year)
print('-='*24)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')