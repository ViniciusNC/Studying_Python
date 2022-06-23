from time import  sleep


def linhas():
    print()
    print('-'*40)
    print('Analisando os valores passados....')


def maior(* num):
    c = maior = 0
    for v in num:
        sleep(0.5)
        print(f'{v}', end=' ')
        if c == 0:
            maior = v
        else:
           if v > maior:
                maior = v
        c += 1
    print(f'\nForam informados {c} valores')
    print(f'O maior valor foi {maior} e foram digitados {len(num)} numeros')


linhas()
print('-' * 40)
maior(2, 9, 4, 5, 7, 1)
linhas()
maior(4, 7, 0)
linhas()
maior(1, 2)
linhas()
maior(6)
linhas()
maior()