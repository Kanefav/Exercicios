soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite O {c} Valor: '))
    if num%2 == 0:
        soma += num
        cont += 1
print(f'Voçe me informou {cont} Números Ìmpares e a soma deles é {soma} ')