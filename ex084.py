ficha = list()
while True:
    nome = str(input('Digite o nome do aluno: ')).strip().upper()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = nota1 + nota2 / 2
    ficha.append([nome, [nota1, nota2], media])
    continuar = str(input('Quer continuar? [S/N] ')).strip()
    if continuar in 'Nn':
        break
print('-='*30)
print(f'{"No":<4}{"NOME":<10}{"MEDIA":>8}')
print('-='*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*30)
    na = int(input('Digite o número do aluno para ver sua nota. (999 interrompe): '))
    if na == 999:
        break
    if na <= len(ficha) - 1:
        print(f'Nota de {ficha[na][0]} as notas são {ficha[na][1]}')