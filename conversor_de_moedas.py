'''Programa para converter moedas
Este Programa fiz na língua materna crioula de Cabo Verde com o intuito de ajudar a comunidade.
Visto que, é a lingua que todos falam lá, teria uma melhor compreensão.'''

moeda = input('Bu kre toca pa "Euro" ou "Dolar"? ')

ecv = float(input('kantu escudu bu teni? '))

if moeda == "Euro":
    euro = ecv / 110
    print(f'Ku {ecv:.0f}$, podi cumpra {euro:.2f}€.')
elif moeda == "Dolar":
    dolar = ecv / 100
    print(f'Ku {ecv:.0f}$, bu ta podi cumpra {dolar:.2f}US$.')
else:
    print('Bu ka scodji ninhum d kes opison')

print('OBRIGADO!!!')



