s = 0
cont = 0
for c in range(1, 6+1):
    n1 = int(input('Digite um número: '))
    if n1 % 2 == 0:
        s += n1
        cont += 1
print(f'A soma dos números pares é {s} você informou apenas {cont} PAR')
