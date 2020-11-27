dinheiro = float(input('Qual o valor das compras? '))
pagamento = float(input('''FORMAS DE PAGAMENTO
[1] a vista dinheiro/cheque
[2] a vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
Qual a forma de pagamento: 
'''))
if pagamento == 1:
    dav = dinheiro  - (dinheiro * 10 / 100)
    print(f'Sua compra de {dinheiro:.2f}R$ vai custar no final {dav:.2f}R$')
elif pagamento == 2:
    cav = dinheiro - (dinheiro * 5 / 100)
    print(f'Sua compra de {dinheiro:.2f}R$ vai custar no final {cav:.2f}')
elif pagamento == 3:
    c2x = dinheiro / 2
    print(f'''Sua compra será divida em 2x parcelas de {c2x:.2f}R$ cada
    Com valor final de {dinheiro}
    ''')
elif pagamento == 4:
    dinheirodesconto = dinheiro - (dinheiro * 20 / 100)
    parcelas = int(input('Em Quantas Parcelas? '))
    ddp = dinheirodesconto / parcelas
    print(f'''Sua compra será parcelada em {parcelas}x de {ddp:.2f}R$ com juros
Sua compra de {dinheiro:.2f}R$ no final vai custar {dinheirodesconto:.2f}R$
    ''')