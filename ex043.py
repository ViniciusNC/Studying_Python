n = 0
s = 0
for c in range(1, 501, 2):
 if c % 3 == 0:
    s = s + 1
    n = n+c
print(f'A soma de todos {s} numeros impares que são divisiveis por 3 de 1 a 500 é {n}')
