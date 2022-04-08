media = 0
cont = 0
maiornumero = 0
menornumero = 0
r = ''
while r != 'N':
    n1 = int(input('Digite um número: '))
    r = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    media += n1
    cont += 1
    if cont == 1:
        maiornumero = menornumero = n1
    else:
        if n1 > maiornumero:
            maiornumero = n1
        if n1 < menornumero:
            menornumero = n1
print(f'Você digitou {cont} números, A media dos números digitados foram {media/cont}')
print(f'O maior número digitado foi {maiornumero} e o menor número digitado foi {menornumero}')
