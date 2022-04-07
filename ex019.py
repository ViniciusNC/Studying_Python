from random import choice
aluno1 = input('Digite o nome do Primeiro Aluno: ')
aluno2 = input('Digite o nome do Segundo Aluno: ')
aluno3 = input('Digite o nome do Terceiro Aluno: ')
aluno4 = input('Digite o nome do Quarto Aluno: ')
tuple1 = (aluno1, aluno2, aluno3, aluno4)
print('O aluno que irá limpar o quadro será: ', choice(tuple1))






