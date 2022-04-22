num = [2, 4, 3, 6]
print(num)
print(f'Essa lista tem {len(num)} elementos')
num.append(5)
num.append(2)
num[0] = 1
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print(f'Agora Essa lista tem {len(num)} elementos')
num.insert(1, 100)
print(f'Na posição 1, adicionei o numero 100 {num}')
num.pop(1)
print(f'Retirei o numero 100 da posição 1 {num}')
num.remove(6)
num.sort()
print(num)
print('OUTRO CÓDIGO')
valores = list()
for cont in range(0, 5):
     valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei os seguintes valores {v}')
print('FIM')
# a = [2, 4, 5, 6]
# b = a
# b[2] = 1
# print(f'Lista A {a}')
# print(f'Lista B {b}')
# b = a[:]
# b[1] = 3
# print(f'Lista A {a}')
# print(f'Lista B com o número 3 na posição 1 {b}')