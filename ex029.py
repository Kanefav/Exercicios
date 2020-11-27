velCarro = int(input('Qual a velocidade do carro? '))
if velCarro > 80:
    multa = ((velCarro - 80) * 7)
    print(f'MULTADO!, Voçe ultrapassou a velocidade permitida que é de 80km/h ')
    print(f'Sua multa será de {multa:.2f}R$')
else:
    print('Tenha um Bom Dia, Dirija com segurança')
