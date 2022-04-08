somaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print(f'------------{p}ª PESSOA------------ ')
    nome = str(input('Digite o nome da pessoa: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('SEXO: [M/F] ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1
print(f'A média de idade do grupo é de {somaidade/4} anos')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
print(f'Tem {totmulher20} mulher com menos de 20 anos')