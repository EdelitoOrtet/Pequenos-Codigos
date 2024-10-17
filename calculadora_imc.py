#Calculadora IMC

from time import sleep
peso = float(input('\033[1mDigite seu peso(kg):\033[m '))
altura = float(input('\033[1mDigite sua altura(m):\033[m '))

print('\033[1;36mCALCULANDO SEU IMC.....\033[m')
sleep(2)

imc = peso / (altura * altura)
print(f'\033[1;34mSeu IMC é de {imc:.1f}\033[m')

if imc < 18.5:
    print('\033[1;31mVocê está abaixo do peso\033[m')
elif 18.5 <= imc < 25:
    print('\033[1;32mO seu peso é ideal\033[m')
elif 25 <= imc < 30:
    print('\033[1;33mVocê está acima do peso\033[m')
    print('\033[1mCuidado, você começar a cuidar da sua alimentação!\033[m')
elif 30 <= imc < 40:
    print('\033[1;31mAtenção para obesidade\033[m')
    print('\033[1mVocê deve procurar ajuda medica\033[m')
else:
    print('\033[1;31mObesidade Mórbida\033[m')
    print('\033[1mPeça ajuda médica urgentemente!\033[m'.upper())
