lista = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    continuar = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Essa é a {lista} lista em ordem decrescente')
if 5 in lista:
    print('Você digitou o valor 5')
else:
    print('Você não digitou o valor 5')