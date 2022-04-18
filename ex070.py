numeros = (int(input('Digite um numero ')),
          int(input('Digite outro numero ')),
          int(input('Digite outro numero ')),
          int(input('Digite outro numero ')))
print(numeros)
print(f'O número 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O número 3 foi digitado na posição {numeros.index(3)+1}ª')
else:
    print('O número 3 não foi digitado')
print('Os valores pares digitados foram ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')