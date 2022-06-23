from time import sleep


def contador(i, p, f):
    print('-'*20)
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(1.0)
    if p < 0:
        p *= -1
    if p == 0:
        print('IMPOSSIVEL COM 0, AJUSTAMOS PARA IR DE 1 EM 1')
        p = 1
    if i < f:
        c = i
        while c <= f:
            print(f'{c}', end=' ')
            sleep(0.5)
            c += p
        print('FIM')
    else:
        c = i
        while c >= f:
            print(f'{c}', end=' ')
            sleep(0.5)
            c -= p
        print('FIM!')


contador(1, 1, 10)
contador(10, 2, 0)
print('-' * 20)
print('Está na hora de personalizar a sua própria contagem> ')
contador(i=int(input('inicio: ')), p=int(input('Pulando de: ')), f=int(input('Fim: ')))