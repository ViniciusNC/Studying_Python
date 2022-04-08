from random import randint
numero = float(input('O computador vai escolher um número de 0 a 10. '
                     '\nTente acertar: '))
aleat = randint(0, 10)
tent = 1
while numero != aleat:
    if numero < aleat:
        numero = float(input('Um pouco mais, tente novamente: '))
        tent += 1
    elif numero > aleat:
        numero = float(input('Um pouco menos, tente novamente: '))
        tent += 1
print(f'Parabéns você acertou o número em {tent} tentativas')
print(f'O computador escolheu o seguinte número: {aleat}')