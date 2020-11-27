num = cont = soma = 0
while num != 999:
    num = int(input('Digite um Número [999 Para Parar]: '))
    soma += num
    cont += 1
print(f'Voçe Digitou {cont - 1} Números e a Soma entre eles é {soma - 999}')