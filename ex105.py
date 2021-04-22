def notas(* notas):
    '''receives many grades from students and returns a list with some informations about the grades'''
    notas = []
    while True:
        notas.append(int(input('Nota:')))
        confirm = input('Alguma outra nota? S/N ')
        if confirm in 'Nnnão':
            break
        else: 
            continue

    # Maior nota
    MaiorNota = notas[0]
    for nota in range(0, len(notas)):
        if notas[nota] > MaiorNota:
            MaiorNota = notas[nota]
    
    # Menor nota
    MenorNota = notas[0]
    for nota in range(0, len(notas)):
        if MenorNota > notas[nota]:
           MenorNota = notas[nota]
    
    # Media 
    TotalNotas = 0

    for nota in range(0, len(notas)):
        TotalNotas += notas[nota]
    MediaNotas = TotalNotas / len(notas)

    # Número de notas
    NumNotas = len(notas)

    print(f'Foram {NumNotas} Notas que são:') 
    print(notas)
    print(f'Maior nota foi {MaiorNota} e a menor foi {MenorNota}')
    print(f'A média das notas foi {MediaNotas:.2f}')


#main program
notas()
