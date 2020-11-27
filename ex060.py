#from math import factorial#
#n = int(input('Digite um Número para Calcular sua Fatorial: '))#
#f = factorial(n)#       ' MANEIRA COM O USO DA FUNÇÂO FACTORIAL '
#print(f'A fatorial de {n} é {f}')#
n = int(input('Digite um Número para Calcular sua Fatorial: '))
c = n
f = 1
print(f'{n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)