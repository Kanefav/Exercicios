p = float(input('qual é o preço do produto? R$'))
d = float(input('quanto é o desconto? % '))
pd = (p * d) /100
print(f'o produto que custava {p:.2f} como o desconto de {d:.2f} vai custar {pd:.2f}')