contmais1000 = maisbarato = total = cont = 0
barato = ''
print('-='*8)
print('Loja Super Baratão')
print('-='*8)
while True:
    cont += 1
    pnome = str(input('Nome do Produto: ')).capitalize()
    preço = float(input('Preço: R$'))
    continuar = str(input('Quer Continuar: [S/N]')).strip()[0].upper()
    total += preço
    if cont == 1:
        maisbarato = preço
        barato = pnome
    else:
        if preço < maisbarato:
            maisbarato = preço
            barato = pnome
    if preço >= 1000:
        contmais1000 += 1
    if continuar == 'S':
        continue
    else:
        break
print('-=-=-=-=FIM DO PROGRAMA-=-=-=-=')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {contmais1000} produto custando mais de R$1000')
print(f'O produto mais barato foi {barato} que custa R${maisbarato:.2f}')