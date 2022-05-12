number = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        number[0].append(valor)
    else:
        number[1].append(valor)
print(f'Os valores digitados foram {number}')
number[0].sort()
print(f'Os valores pares são: {number[0]}')
number[1].sort()
print(f'Os valores ímpares são: {number[1]}')