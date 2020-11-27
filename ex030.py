numero = int(input('Escreva um número qualquer: '))
resultado = (numero % 2)
if resultado == 1:
    print(f'O número {numero} é Ìmpar')
elif resultado == 0:
    print(f'O número {numero} é Par')