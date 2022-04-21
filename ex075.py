lista = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da fila.... ')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Numero adicionado na posição {pos}º da lista...')
                break
            pos += 1
print(f'Os números digitados na ordem foram {lista}')
