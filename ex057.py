print('SEQUÊNCIA DE FIBONACCI')
t1 = 0
t2 = 1
termo = int(input('Quantos termos você deseja ver? '))
cont = 0
print(f'{t1} - {t2}', end='')
while cont != termo:
    cont += 1
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(f' - {t3}', end='')
print('\nFIM')
