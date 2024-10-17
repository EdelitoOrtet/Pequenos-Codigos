#Calculadora IMC

def IMC (peso, altura):

    imc = peso / (altura * altura)
    return imc

IMC(68, 1.72)
print(f'O seu IMC é {IMC(68, 1.72):.2f}')