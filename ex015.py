dias = float(input('quantos dias vc alugou o carro? '))
km = float(input('quantos km vc rodou com ele? '))
diavalor = 60 * dias
kmvalor = 0.15 * km
diakmvalor = diavalor + kmvalor
print(f'o total a pagar é R${diakmvalor:.2f}')