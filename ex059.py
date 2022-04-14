termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
c = 1
total = 0
maistermo = 10
while maistermo != 0:
    total = total + maistermo
    while c <= total:
        print(f'{termo} - ', end='')
        c += 1
        termo += razao
    print('PAUSA')
    maistermo = int(input('\nQuantos termos você quer mostrar a mais? '))
print(f'PA finalizada com {total} termos mostrados')