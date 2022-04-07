from datetime import date
s = 0
a = 0
for i in range(1, 8):
    atual = date.today().year
    nasc = int(input(f'Em que ano a {i}º pessoa nasceu: '))
    idade = atual - nasc
    if idade >= 21:
        s += 1
    else:
        a += 1
print(f'Temos {s} pessoas maiores de idade e {a} menores de idade')
