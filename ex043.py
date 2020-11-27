peso = float(input('Qual o seu peso? (kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / (altura ** 2)
print(f'O seu IMC é {imc:.1f}')
if imc <= 18.5:
    print('Voçe está abaixo do peso normal! Cuidado')
elif imc > 18.5 and imc <= 25:
    print('Voçe está no peso ideal! Parabens')
elif imc > 25 and imc <=30:
    print('Voçe está sobre o peso ideal! Cuidado')
elif imc > 30 and imc <= 40:
    print('Voçe está com obesidade! Cuidado')
else:
    print('Voçe está com obesidade morbida!! Muito Cuidado!')