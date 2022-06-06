aluno = dict()
for c in range(0, 3):
    aluno['nome'] = str(input('Nome: '))
    aluno['media'] = int(input('Média: '))
    if aluno["media"] < 7:
        aluno['situação'] = 'reprovado'
    elif aluno['media'] >= 7:
        aluno['situação'] = 'aprovado'
    for k, v in aluno.items():
     print(f'{k} = {v}')
