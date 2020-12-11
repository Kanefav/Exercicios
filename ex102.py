def fatorial(num = 1, show = False):
        if num == 1:
            if show == True:
                print('1 = ', end='')
            return num
        if show == True:
            print(f'{num} X ', end='')
        return num * fatorial(num - 1, show)


#Main Program
numfatorial = int(input('Digite um numero para fatorar: '))
showfatorial = input('Quer mostrar o precesso? SIM OU NAO').upper()
if showfatorial in 'SIM':
    print(fatorial(numfatorial, True))
else:
    print(fatorial(numfatorial))