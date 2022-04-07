numero = int(input('Digite um número até 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 %10
print(f'Unidade: {u}'
      f'\nDezenas: {d}'
      f'\nCentenas: {c}'
      f'\nMilhar: {m}'
      )


