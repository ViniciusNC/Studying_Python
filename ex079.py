galera = list()
dados = list()
pesomai = pesomen = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(galera) == 0:
        pesomai = pesomen = dados[1]
    else:
        if dados[1] > pesomai:
            pesomai = dados[1]
        if dados[1] < pesomai:
            pesomen = dados[1]
    galera.append(dados[:])
    dados.clear()
    continuar = str(input('Deseja continuar?  [S/N] ')).upper().strip()
    while continuar not in 'SsnN':
        continuar = str(input('Digite S ou N para continuar: ')).strip().upper()
    if continuar in 'nN':
        break
print('=-'*30)
print(f'Estes foram os dados que digitados: {galera}')
print(f'Ao todo você cadastrou: {len(galera)} pessoas')
print(f'O maior peso foi de {pesomai}KG. Peso de ', end='')
for p in galera:
    if p[1] == pesomai:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {pesomen}KG. Peso de ', end='')
for p in galera:
    if p[1] == pesomen:
        print(f'{p[0]} ', end='')
print()