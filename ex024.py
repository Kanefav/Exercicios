cidade = str(input('em que cidade vc nasceu?')).strip()
lista = [cidade]
cidade.split()
if cidade[:6].upper() == 'SANTOS':
    print('true')
else:
    print('false')