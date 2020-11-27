palavra = ('aprender', 'programa', 'linguagem', 'python',
           'curso', 'Gratis', 'estudar', 'praticar',
           'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavra:
    print(f'\nNa Palavra {p} Temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
