tabuada = int(input('Quer ver a tabuada de qual valor? '))
resultado = 1
while True:
    if tabuada < 0:
        break
    for cont in range(1, 11):
        resultado = tabuada * cont
        print(f'{tabuada} X {cont} = {resultado}')
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    if tabuada < 0:
        break
print('FIM DA TABUADA')