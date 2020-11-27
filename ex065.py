resp = 'S'
cont = soma = media = maior = menor = 0
while resp == 'S':
    cont += 1
    num = int(input('Digite um Número: '))
    resp = str(input('Quer Continuar? [S/N] ')).upper().strip()[0]
    soma += num
    if num > maior:
        maior = num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / cont
print(f'Voçe Digitou {cont} Números e a Média foi de {media:.1f} ')
print(f'O Maior Valor foi {maior} e o Menor Foi {menor}')