lista = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}o. Valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
    valor = 0
print('-='*16)
print(f'Os valores pares digitados foram {lista[0]}')
print(f'Os valores pares digitados foram {lista[1]}')