termo = int(input('Digite o termo da PA: '))
razao = int(input('Digite a razao da PA: '))
cont = 0
while cont < 10:
    print(f'{termo} - ', end='')
    termo += razao
    cont += 1
print('FIM')