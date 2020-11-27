tabuada = cont = 0
while True:
    num = int(input('Quer ver a tabuada de qual valor: '))
    if cont == 10:
        cont -= 10
    if num <= -1:
        break
    for c in range(1, 11):
        tabuada = num * c
        print(f'{num} x {c} = {tabuada}')
print('PROGRAMA TABUADA ENCERRADO! VOLTE SEMPRE!')