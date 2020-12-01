from random import randint


def sorteia(lista):
    for c in range(0, 5):
        lista.append(randint(1, 10))
    print(lista)


def somapar(lista):
    soma = 0
    for num in range(0, len(lista)):
        if lista[num] % 2 == 0:
            soma += lista[num]
    print(f'A soma dos pares foi {soma}')


# Main Program
numeros = list()
sorteia(numeros)
somapar(numeros)