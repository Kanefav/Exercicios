num = (int(input('Digite um Número:')),
      int(input('Digite um Número: ')),
      int(input('Digite um Número: ')),
      int(input('Digite um Número: ')))
print(f'Voçe digitou os valores: {num}')
print(f'O valor 9 apareceu {num.count(9)}')
if 3 in num:
    print(f'O valor 3 apareceu na posição {num.index(3) + 1}')
else:
    print('O valor 3 nao apareceu em nenhuma posição')
print('Os valores pares ', end='')
for c in num:
    if c % 2 == 0:
        print(c, end=' ')
