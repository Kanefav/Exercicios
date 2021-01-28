preco = float(input('qual é o preço do produto? R$'))
desconto = float(input('quanto é o desconto? % '))
TempDesconto = preco*desconto / 100
PrecoDesconto = preco - TempDesconto

print(f'o produto que custava {preco:.2f} como o desconto de {desconto}% vai custar {PrecoDesconto:.2f}')