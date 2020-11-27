n1 = float(input("uma distancia em metros: "))
n2 = n1*100
n3 = n1*1000
n4 = n1*10000
n5 = n1/100
n6 = n1/1000
n7 = n1/10000

print(f'uma distancia de {n1}m corresponde a:')
print(f'{n2:.1f}dm')
print(f'{n3:.1f}cm')
print(f'{n4:.1f}mm')
print(f'{n5:.1f}dam')
print(f'{n6:.1f}hm')
print(f'{n7:.1f}km')


