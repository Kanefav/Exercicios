ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar [S/N]? ')).upper()
    if resp == 'N':
        break
    else:
        continue
print('-='*24)
print(f'{"No.":<4}{"NOME":<10}{"MÈDIA":>8}')
print('-'*20)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('-'*20)
while True:
    mostnota = int(input('Mostrar Notas de qual aluno? (999 interrompe) '))
    if mostnota == 999:
        break
    if mostnota <= len(ficha) - 1:
        print(f'Notas de {ficha[mostnota][0]} {ficha[mostnota][1]} ')
