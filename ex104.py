def LeiaInt(n):
    ok = False
    valor = 0
    while True:
        n = input(n)
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Erro! Isso não é um Numero')
        if ok:
            break
    return valor
        
    

#Main Program
n = LeiaInt('Digite um Numero: ')
print(f'Você digitou o Numero {n} ')
