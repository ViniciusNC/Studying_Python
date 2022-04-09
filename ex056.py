n1 = int(input('Digite um número para calcular seu fatorial: '))
c = n1
f = 1
print(f'Calculando fatorial de {n1}!: ')
while c > 0:
    print(f'{c}', end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
