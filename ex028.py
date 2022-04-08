from random import randint
numero = float(input('O computador vai escolher um número de 0 a 10. Tente acertar!: '))
aleat = randint(0, 10)
while numero != aleat:
    numero = float(input('Tente novamente: '))
print('Parabéns você acertou o número')
print(f'O computador escolheu o seguinte número: {aleat}')
