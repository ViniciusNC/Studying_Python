maiornumero = 0
soma = 0
multi = 0
r = 0
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
while r != 5:
    r = int(input('1 Somar'
                 '\n2 Multiplicar'
                 '\n3 Maior número'
                 '\n4 Novos Números'
                 '\n5 Sair do programa'
                  '\nDeseja escolher qual opção?: '))
    if r == 1:
        soma = n1 + n2
        print(f'---------------------------------------'
              f'\nA soma entre {n1} + {n2} é: {soma}'
              f'\n--------------------------------------')
    elif r == 2:
        multi = n1 * n2
        print(f'---------------------------------------'
              f'\nA multiplicação entre {n1} * {n2} é: {multi}'
              f'\n--------------------------------------')
    elif r == 3:
        if n1 > n2:
            maiornumero = n1
            print(f'---------------------------------------'
                  f'\nO Maior número é {n1} o primeiro valor digitado'
                  f'\n--------------------------------------')
        elif n2 > n1:
            maiornumero = n2
            print(f'--------------------------------------'
                  f'\nO maior número é {n2} o segundo valor digitado'
                  f'\n--------------------------------------')
    elif r == 4:
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
    else:
        print('OPÇÃO INVALIDA. TENTE NOVAMENTE')
print('PROGRAMA FECHADO')