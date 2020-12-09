from datetime import date
def votar(nasceu):
    global idade
    idade = ano - nasceu
    if idade >= 17:
        return True

#Main Program
ano = date.today().year
nasceu = int(input('Em que ano vc nasceu? '))
if votar(nasceu) == True:
    print(f'Com {idade} anos: Voto obrigatório')
else:
    print('KIDZIN KIDZAO ME DA UM MAMAO')