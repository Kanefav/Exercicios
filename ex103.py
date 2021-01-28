jogador = ""
numerogols = ""
fichajog = {'Jogador': jogador, 'Numerogols': numerogols}


def ficha():
    fichajog["Jogador"] = str(input('Nome do jogador:'))
    if fichajog["Jogador"] == "":
        fichajog["Jogador"] = "desconhecido"
    fichajog["Numerogols"] = str(input('Numero de gols marcados: '))
    if fichajog["Numerogols"] == "" :
        fichajog["Numerogols"] == "0"
    print(f'O jogador {fichajog["Jogador"]} marcou {fichajog["Numerogols"]} gols no campeonato.')


#Main Program
ficha()