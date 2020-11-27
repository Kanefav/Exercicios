print('='*16)
print('        10 TERMOS DE UMA PA')
print('='*16)
ptermo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = ptermo + (10 - 1) * razao
for c in range(ptermo, decimo, razao):
    print(c, end=' ')
print('ACABOU')
