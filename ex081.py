lista = []
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    continuar = str(input('Quer Continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
    else:
        continue
print(f'Você digitou {cont} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente {lista}')
if 5 in lista:
    print('5 está na lista')
else:
    print('5 não está na lista')


