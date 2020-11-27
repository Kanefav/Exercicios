cont = soma = 0
while True:
    num = int(input('Digite um número: [999 para parar] '))
    cont += 1
    if num == 999:
        break
    soma += num
print(f'A soma dos {cont} foi de {soma}')