lista = []
lista2 = []
lista3 = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if n % 2 == 0:
        lista2.append(n)
    else:
        lista3.append(n)
    if 'N' in continuar:
        break
print(lista)
print(lista2)
print(lista3)
