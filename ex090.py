aluno = {}
aluno['Nome'] = str(input('Nome: ')).capitalize()
aluno['Media'] = float(input(f'Média de {aluno["Nome"]}: '))
print('-='*24)
if aluno['Media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['Media'] > 3 < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print(f'  - nome é igual a {aluno["Nome"]}')
print(f'  - média é igual a {aluno["Media"]}')
print(f'  - situação é igual a {aluno["situação"]}')