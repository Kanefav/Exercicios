def soma(a, b):
    print(f'A = {a} B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


#programa principal
soma(4, 5)
soma(7, 8)


# * = tuplas
def contador(* num):
    tam = len(num)
    print(f'Recebi os numeros {num} e ao todo são {tam}')


#programa principal
contador(1, 3, 5, 7)
contador(3, 6, 9)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


lista = [3, 5, 6, 8, 2, 4]
dobra(lista)
print(lista)
