homem = 0
mulher = 0
totalidade = 0
while True:
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo: F/M ')).strip().upper()[0]
    print('-' * 20)
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    print('-' * 20)
    if sexo in 'M':
        homem += 1
    if sexo in 'F' and idade < 20:
        mulher += 1
    if idade > 18:
        totalidade += 1
    if continuar in 'N':
        break
print(f'Ao todo temos {homem} homens cadastrado')
print(f'Total de pessoas com mais de 18 anos: {totalidade}')
print(f'E temos {mulher} mulheres com menos de 20 anos')