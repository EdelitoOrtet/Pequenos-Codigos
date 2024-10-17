import random
conta_vitorias = 0
print('\033[1;33m-=-' * 15)
print(' '*10,'\033[1;34mJOGO DO PAR OU IMPAR\033[m')
print('\033[1;33m-=-\033[m' * 15)

while True:
    numero = int(input('\033[1mEscolhe um número de 0 a 10: '))
    sua_jogada = input('PAR ou IMPAR? [P/I]: ').upper().strip()
    computador = random.randrange(11)
    total = numero + computador
    if total % 2 == 0:
        if sua_jogada == 'P':
            print('\033[1;32mVOCÊ VENCEU!\033[m')
            print(f'\033[1mVocê escolheu {numero} e o computador escolheu {computador}')
            print(f'O resultado é {total} e é\033[m \033[1;32mPAR\033[m')
            conta_vitorias += 1

        elif sua_jogada == 'I':
            print('\033[1;31mVOCÊ PERDEU\033[m')
            print(f'\033[1mVocê escolheu {numero} e o computador escolheu {computador}')
            print(f'O resultado é {total} e é\033[m \033[1;31mPAR\033[m')
            break

    elif total % 2 == 1:
        if sua_jogada == 'I':
            print('\033[1;32mVOCÊ VENCEU\033[m')
            print(f'\033[1mVocê escolheu {numero} e o computador escolheu {computador}')
            print(f'O resultado é {total} e é\033[m \033[1;32mÍMPAR\033[m')
            conta_vitorias += 1

        elif sua_jogada == 'P':
            print('\033[1;31mVOCÊ PERDEU\033[m')
            print(f'\033[1mVocê escolheu {numero} e o computador escolheu {computador}')
            print(f'O resultado é {total} e é\033[m \033[1;31mÍMPAR\033[m')
            break

print(f'\033[1;34mGAME OVER!!!\033[m \033[1mVocê terminou o jogo com \033[32m{conta_vitorias} vitória(s)\033[m')

