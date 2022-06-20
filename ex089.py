pessoas = list()
pessoa1 = dict()
soma = media = 0
while True:
    pessoa1.clear()
    pessoa1['nome'] = str(input('Nome: ')).strip().upper()
    while True:
        pessoa1['sexo'] = str(input('Sexo : [M/F] ')).strip().upper()
        if pessoa1['sexo'] in 'MF':
            break
        print('ERRO" digite apenas M ou F')
    pessoa1['idade'] = int(input('Idade: '))
    soma += pessoa1['idade']
    pessoas.append(pessoa1.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! RESPONDA COM S OU N')
    if resp == 'N':
        break
print(f'Ao todo temos {len(pessoas)} pessoas cadastradas')
media = soma / len(pessoas)
print(f'A média das pessoas cadastras é de {media:5.2f} anos.')
print('As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}, ', end='')
print()
print('Lista das pessoas acima da média: ')
for p in pessoas:
    if p['idade'] >= media:
        print('  ', end='')
        for i, k in p.items():
            print(f'{i} == {k}: ', end='')
            print()
