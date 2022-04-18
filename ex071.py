produtos = ('Lapis', 2.50,
                'Caderno', 15,
                'Lapiseria', 5,
                'Borracha', 3,
                'Fichário', 20)
print('-'*40)
print(f'{"Listagem de Preço":^40}')
print('-'*40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')

