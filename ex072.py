cont = ('Zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco',
        'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
        'Onze', 'Doze','Treze', 'Quatorze',
        'Quinze', 'Dezesseis', 'Dezessete',
        'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um Número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    else:
        print('Tente Novamente. ', end='')
        continue
print(f'Voçe digitou o número {cont[num]}')