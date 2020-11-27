lista = []
tlist = 0
while True:
    num = lista.append(int(input('Digite um valor: ')))
    cont = str(input('Quer continuar? [S/N] ')).upper()
    if cont == 'N':
        break
    else:
        continue
lista.sort()
print(lista)
