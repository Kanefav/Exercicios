frase = str(input('Digite uma frase: ')).strip().upper()
fraseA = frase.count('A')
frase1a = frase.find('A')+1
frase2a = frase.rfind('A')+1
print(f'A letra a aparece {fraseA} nessa frase ')
print(f'A primeira letra a estava na posição {frase1a}')
print(f'E a ultima letra apareceu na posição {frase2a} ')
