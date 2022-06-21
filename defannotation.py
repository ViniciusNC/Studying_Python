def double(lst):
    pos = 0
    while pos < len(lst):
            lst[pos] *= 2
            pos += 1


valores = list()
for c in range(0, 2):
   valores.append(int(input('Digite um número: ')))
double(valores)
print(valores)
