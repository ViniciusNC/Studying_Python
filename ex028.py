from random import randint
numero = float(input('O computador vai escolher um número de 0 a 5. Tente acertar!: '))
aleat = randint(0, 5)
print(f'O computador escolheu o seguinte número: {aleat}')
print('Parabéns você acertou o número'if numero == aleat else "Você errou, tente novamente")

