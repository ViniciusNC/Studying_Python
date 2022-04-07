velocidade = float(input('Em que velocidade estava seu carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Seu carro ultrapassou 80Km/h, será multado!'
          f'\nO valor da multa é de: {multa:.2f} R$')
else:
    print(' Estava na velocidade correta!')