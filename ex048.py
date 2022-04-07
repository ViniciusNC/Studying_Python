t = int(input('Digite o Primeiro termo da PA: '))
r = int(input('Digite a RAZÃO DA PA: '))
dec = t + (10 - 1) * r
for c in range(t, dec + r, r):
    print(c, end=' ')

