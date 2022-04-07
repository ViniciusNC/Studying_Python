n1 = int(input('Digite um número: '))
tot = 0
for c in range(1, n1+1):
    if n1 % c == 0:
        print(c, end=' ')
        tot += 1
print(f'\n O número {n1} foi divisivel {tot} vezes')
if tot == 2:
    print('Por isso ele é primo')
else:
    print('Por isso ele não é primo')