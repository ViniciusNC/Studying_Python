maisquemil = total = maisbarato = cont = 0
produtomaisbarato = ''
while True:
    produto = str(input('Digite o nome do produto: ')).strip().title()
    preco = float(input('Digite o valor do produto: R$'))
    cont += 1   
    total += preco
    if cont == 1:
        maisbarato = preco
        produtomaisbarato = produto
    else:
        if preco < maisbarato:
            maisbarato = preco
            produtomaisbarato = produto
    if preco > 1000:
        maisquemil += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
print('FIM DO PROGRAMA')
print(f'O total da compra foi de R${total:.2f}')
print(f'Temos {maisquemil} produto custando mais que R$1000.00')
print(f'O produto mais barato foi {produtomaisbarato} que custa R${maisbarato}')
