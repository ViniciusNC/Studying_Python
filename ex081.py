matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for line in range(0, 3):
    for c in range(0, 3):
        matriz[line][c] = int(input(f'Digite um valor para [{line}][{c}]: '))
for line in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[line][c]:^5}]', end='')
    print()