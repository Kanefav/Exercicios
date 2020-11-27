from random import randint
print('-=-'*24)
print('Vou pensar em um número de 0 a 5. Tente adivinhar... ')
print('-=-'*24)
Computador = randint(0, 5)
Número = int(input('Em que número eu pensei? ')).strip()
if Número == Computador:
    print(f'Parabens Voçe Conseguiu o número foi {Computador}')
else:
    print(f'Que pena Voçe não conseguiu o número era {Computador} ')