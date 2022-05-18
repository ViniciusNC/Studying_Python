matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for line in range(0, 3):
    for c in range(0, 3):
        matriz[line][c] = int(input(f'Digite um valor para [{line}][{c}]: '))
for line in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[line][c]:^5}]', end='')
        if matriz[line][c] % 2 == 0:
            spar += matriz[line][c]
    print()
print('-='*30)
print(f'A soma dos valores pares é {spar}')
for line in range(0, 3):
    scol += matriz[line][2]
print(f"A soma dos valores da terceira coluna é {scol}")
for c in range(0, 3):
    if c == 0 or matriz[1][c] > mai:
        mai = matriz[1][c]
print(f' O maior valor da segunda coluna é {mai}')
