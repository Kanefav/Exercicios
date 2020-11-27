def cont(i, f, p):
    if i > f:
        print(f'Contagem de {f} até {i} de {p} em {p}')
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            cont -= p
    else:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            cont += p
    print('Fim')


# Main
cont(0, 10, 1)
cont(10, 0, 2)
print('Agora é sua vez de personalizar a contagem')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
cont(i, f, p)
