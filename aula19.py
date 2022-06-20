# pessoas = {'nome': 'Vinicius', 'sexo': 'M', 'idade': 20}
# pessoas['peso'] = 55
# for k, v in pessoas.items():
#     print(f'{k} = {v}')

# brasil = []
# estado1 = {'UF': 'RJ'}
# estado2 = {'UF': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(brasil[0])

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['Sigla'] = str(input('Sigla: '))
    estado['UF'] = str(input('Unidade federativa: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}')
