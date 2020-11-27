valores = []
for cont in range(0, 5):
    valor = valores.append(int(input('Digite um Número Inteiro: ')))

for c, v in enumerate(valores):
    print(f'Na Posição {c} Encontrei o Valor {v}!')
print('Cheguei ao final da minha lista')
# lista.append() adicona por ultimo
#lista.insert(0, ) o primeiro numero é a posição(exemplo 0)
#lista.pop(0) apaga a posição definida(exemplo 0)
#lista.remove(45) apaga algo da lista se tiver(exemplo, numero 45)
#lista.sort() deixa em ordem crescente
#lista.sort(reverse=True)