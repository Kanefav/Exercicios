print('-='*16)
print('Seguencia de Fibonacci')
print('-='*16)
vezes = int(input('Quantos Termos Voçe quer Mostrar? '))
t1 = 0
t2 = 1
print(f'{t1} - {t2}', end='')
while vezes != 0:
    t3 = t1 + t2
    print(f' - {t3}', end='')
    t1 = t2
    t2 = t3
    vezes -= 1
print(' - fim')