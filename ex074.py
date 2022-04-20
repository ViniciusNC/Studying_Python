lista = list()
while True:
    n = int(input('Digite um numero: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Não vou adicionar, valor duplicado!')
    continuar = str(input('Quer continuar: [S/N] ')).lower().strip()
    while continuar not in 'SsnN':
        continuar = str(input('Digite [S/N] para continuar ')).lower().strip()
    if continuar in 'n':
        break
lista.sort()
print(f'Você digitou os valores: {lista}')
