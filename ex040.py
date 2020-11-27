nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1} e {nota2}, a média do aluno é {media:.2f} ')
if media > 7:
    print('O aluno está APROVADO')
else:
    print('O aluno está REPROVADO')