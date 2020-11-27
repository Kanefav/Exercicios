casav = float(input('Qual o valor da casa? '))
salario = float(input('Qual o valor de seu salário? '))
anos = float(input('Quantos anos de financiamento? '))
prestacao = casav / (anos * 12)
if prestacao > salario + (salario * 30 / 100):
    print(f'Empréstimo negado')
else:
    print(f'Emprestimo aceito a prestação será de {prestacao:.2f}R$ por mês')