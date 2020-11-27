num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão
[1] - BINÁRIO
[2] - OCTAL
[3] - HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{num} convertido para BINÀRIO é {bin(num)}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é {oct(num)}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é {hex(num)}')
else:
    print(f'Nenhuma opção foi selecinada')