n1 = float(input('Digite um valor: '))
n2 = float(input('Digite um segundo valor: '))
s = n1+n2
sub = n1-n2
m = n1*n2
d = n1/n2
di = n1//n2
p = n1**n2
print(f'A soma é \n {s}, o produto é {m} e a divisão é {d:.3f}', end=' ')
print(f'Divisão inteira {di} e potência {p}')
print(f'Se a potência dos valores é {p} e a soma é {s} então a potência menos a soma vai ser: {p-s}')
