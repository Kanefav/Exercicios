# How to know if you will receive to many parameter in def? insert one * in def, be like this:
def maior(* num):
    cont = 0
    maior = num[0]
    print(f'Numeros recebidos: {num}')
    for pos in range(0, len(num)):
        cont += 1
        if maior < num[pos]:
            maior = num[pos]
    print(f'O maior numero obtido foi {maior}')



# Main Program
maior(2, 1, 4, 20, 5)
maior(-2, 4, 2, -3, 9)