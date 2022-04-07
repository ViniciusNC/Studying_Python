from random import shuffle
aluno1 = str(input('Digite o nome do Primeiro Aluno: '))
aluno2 = str(input('Digite o nome do Segundo Aluno: '))
aluno3 = str(input('Digite o nome do Terceiro Aluno: '))
aluno4 = str(input('Digite o nome do Quarto Aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print('A ordem de apresentação irá ser: ')
print(lista)





