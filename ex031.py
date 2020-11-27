distancia = float(input('Quantos Km será a Viagem: '))
if distancia < 201:
    custo200 = distancia * 0.50
    print(f'O custo de sua viagem será de {custo200:.2f}R$')
elif distancia > 201:
    custo201 = distancia * 0.45
    print(f'O custo da viagem será de {custo201:.2f}R$')