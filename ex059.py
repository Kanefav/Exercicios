n1 = float(input('Primeiro Número: '))
n2 = float(input('Segundo Número: '))
programa = False
print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do Programa
   ''')
while not programa:
    opcao = input('Qual Sua opção: ').strip()
    if opcao == '1':
        resultado = n1 + n2
        print(f'A Soma de {n1:.2f} + {n2} è {resultado:.2f}')
    if opcao == '2':
        resultado = n1 * n2
        print(f'A Multiplicação de {n1:2f} e {n2:.2f} é {resultado:.2f}')
    if opcao == '3':
        if n1 > n2:
            resultado == n1
            print(f'O Maior Entre {n1:.2f} e {n2:.2f} é {resultado:.2f}')
        if n2 > n1:
            resultado == n2
            print(f'O Maior Entre {n1:.2f} e {n2:.2f} é {resultado:.2f}')
        else:
            print('São Iguais')
    if opcao == '4':
        n1 = float(input('Primeiro Número: '))
        n2 = float(input('Segundo Número: '))
    if opcao == '5':
        programa = True
print('Fim do Programa! Volte Sempre!')
