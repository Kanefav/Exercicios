#dicionarios
# Dicionario = dict()           ou
dicionario = {'Nome': 'Jão', 'Idade': '29', 'Peso': '78'}
print(dicionario.values(), end=' ')
print()
print(dicionario.items(), end=' ')
print()
print(dicionario.keys(), end=' ')
print()
#para apagar um item
del dicionario['Nome']
print(dicionario)
#para adicionar um item
dicionario['Nome'] = str(input('Nome: '))
print(dicionario['Nome'])

