#Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep
from random import choice

titulo = '\033[1mJOGO PEDRA PAPEL E TESOURA'
print(titulo.center(30, "="))

print(''' Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogada = ['PEDRA', 'PAPEL', 'TESOURA']
jogador = int(input('Sua jogada: '))
computador = choice(jogada)

print('\033[1;35mJO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!!!\033[m')

print('-=' * 15)
if jogador == 0 and computador == 'TESOURA': #jogador jogou PEDRA
    print(f'Jogadador jogou \033[1;32m{jogada[0]}\033[m')
    print(f'Computador jogou \033[1;31mTESOURA\033[m')
    print('-=' * 15)
    print('\033[1;32mJOGADOR VENCEU\033[m')
elif jogador == 1 and computador == 'PEDRA':#jogador jogou PAPEL
    print(f'Jogador jogou \033[1;32m{jogada[1]}\033[m')
    print(f'Computador jogou \033[1;31mPEDRA\033[m')
    print('-=' * 15)
    print('\033[1;32mJOGADOR VENCEU\033[m')
elif jogador == 2 and computador == 'PAPEL':#jogador jogou TESOURA
    print(f'Jogador jogou \033[1;32m{jogada[2]}\033[m')
    print(f'Computador jogou \033[1;31mPAPEL\033[m')
    print('-=' * 15)
    print('\033[1;32mJOGADOR VENCEU\033[m')
elif jogada[jogador] == computador:
    print(f'O jogador jogou \033[1;32m{jogada[jogador]}\033[m')
    print(f'Computador jogou \033[1;31m{computador}\033[m')
    print('-=' * 15)
    print('\033[1;34mEMPATE\033[m')
else:
    print(f'Jogador jogou \033[1;32m{jogada[jogador]}\033[m')
    print(f'Computador jogou \033[1;31m{computador}\033[m')
    print('-=' * 15)
    print('\033[1;31mCOMPUTADOR VENCEU\033[m')



