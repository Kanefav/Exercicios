#lanche = ('Macarrão', 'Suco de Laranja', 'Chocolate') maneira antiga de fazer tuplas
lanche = 'Macarrão', 'Suco de Laranja', 'Chocolate'
for c in lanche:
    print(c)
for c in range(0, len(lanche)):
    print(lanche[c])
for pos, c in enumerate(lanche):
    print(f'{c} na posição {pos}')