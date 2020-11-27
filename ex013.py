print('responde as perguntas corretamente (sim,não)')
salar = float(input('qual é o salario do funcionario? R$'))
aument = str(input('o seu salario vai sofrer um aumento?'))
if aument == 'sim':
    salar2 = float(input('de quantos % será esse aumento:'))
    salar3 = salar + (salar * salar2 /100)
    exit(code=print(f'o salario desse funcionario que era R${salar:.2f} será aumentado para R${salar3:.2f}'))
if aument == 'não':
    salar4 = str(input('o salario desse funcionario será reduzido? '))
if salar4 == 'não':
    salar5 = str(input('o salario desse funcionario recebera alguma alteração? '))
if salar4 =='não':
    print(f'então o salario do funcionario será de R${salar:.2f}')
elif salar4 == 'sim':
    salar6 = float(input('de quantos % será a redução do salario do funcionario?'))
    salar7 = salar - (salar * salar6/100)
    print(f'o valor do salario do funcionario de R${salar:.2f} será reduzido para R${salar7:.2f}')