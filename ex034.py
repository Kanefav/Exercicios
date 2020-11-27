salario = float(input('Qual é o salário do Funcionário? R$ '))
if salario < 1250 :
    aumento1250 = salario + (salario * 15 / 100)
    print(f'O salário agora é {aumento1250:.2f}R$')
else:
    aumentobaixo = salario + (salario * 10 / 100 )
    print(f'O salário agora é {aumentobaixo:.2f}R$')
