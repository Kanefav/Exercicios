def area(a, b):
    area = a * b
    print(f'A área de um terreno {a:.1f}x{b:.1f} é de {area:.1f}m²')


print('Controle de terrrenos')
print('-='*18)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)