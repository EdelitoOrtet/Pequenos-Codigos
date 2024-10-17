from random import randint
from time import sleep

print('\033[34m=--=\033[m'*15)
print('\033[1mJOGO DE ADVINHAÇÃO\033[m')
print('\033[1mVou pensar em um número entre 0 e 10. Tente adivinhar...\033[m')
print('\033[34m=--=\033[m'*15)

computador = randint (0, 10)
jogador = int(input('\033[1mEm que número eu pensei?\033[m '))
print('\033[1;35mPROCESSANDO...\033[m')
sleep(1)
tentativas = 0

while jogador != computador:
    print('\033[1;31mERROU!!!!\033[m')
    if jogador < computador:
        print('Mais... Tente mais uma vez!')
    else:
        print('Menos... Tente mais uma vez!')
    jogador = int(input(f'\033[1mEm que número estou a pensar?\033[m '))
    print('\033[1;35mPROCESSANDO...\033[m')
    sleep(1)

    if jogador == computador:
        print('\033[1;32mPARABÉNS!!!\033[m')
    tentativas += 1

print(f'\033[1mVocê acertou depois de {tentativas} tentativas.\033[m')