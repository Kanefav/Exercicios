nome = str(input('Qual seu nome: ')).strip().upper()

if nome in ('ENZO GABRIEL RAFAEL MIGUEL PEDRO MARIA JOAO '):
    print('Seu nome é popular no Brasil')
    nome = nome.capitalize()
    print(f'Bom dia {nome}')
elif nome in ('CREUZA, CASSIO, JULHO'):
    print('Seu nome é bem incomum ')
    nome = nome.capitalize()
    print(f'Bom dia {nome}')

else:
    nome = nome.capitalize()
    print('Seu nome é bem comum')
    print(f'Bom dia {nome}')
