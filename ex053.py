frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
print(f'Voçe digitou a frase {junto}')
for c in range(len(junto)-1, -1, -1):
    inverso += junto[c]
print(junto, inverso)
if junto == inverso:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')