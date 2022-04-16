import random
print('JOGO DE PAR OU ÍMPAR')
jogos = 0
while True:
    n = int(input('Digite um valor: '))
    computador = random.randint(0, 10)
    total = n + computador
    parouimpar = ' '
    while parouimpar not in 'PI':
        parouimpar = str(input('PAR OU ÍMPAR? [P/I] ')).strip().upper()[0]
    if total % 2 == 0:
        print(f'Você jogou {n} e o computador {computador}. Total de {total} DEU PAR')
        if parouimpar in 'P':
            jogos += 1
            print('VOCÊ VENCEU')
        elif parouimpar in 'I':
            print('VOCÊ PERDEU')
            break
    else:
        print(f'Você jogou {n} e o computador {computador}. Total de {total} DEU ÍMPAR')
        if parouimpar in 'I':
            jogos += 1
            print('VOCÊ VENCEU')
        elif parouimpar in 'P':
            print('VOCE PERDEU')
            break
print(f'GAME OVER! Você venceu {jogos} vezes')

