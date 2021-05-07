from time import sleep
def ajuda(comando):
    help(comando)


# Main Program 
print('Iniciando Programa...')
sleep(1)
while True:
    InicioAjuda = str(input('Função ou Biblioteca: // Digite Fim para encerrar ')).lower()
    if InicioAjuda == 'fim':
        break
    else:
        ajuda(InicioAjuda)
print('Programa Encerrado')