numeros = list()
for cont in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a posição {cont}: ')))
print('-='*30)
print('Você digitou os valores: ', end='')
print(*numeros, sep=',')
print('-='*30)
print(f'O maior número digitado foi {max(numeros)} nas posições: ', end='')
for c, v in enumerate(numeros):
    if v == max(numeros):
        print(f'{c}...', end='')
print(f'\nO menor número digitado foi {min(numeros)} na posição: ', end='')
for c, v in enumerate(numeros):
    if v == min(numeros):
        print(f'{c}...', end='')
print('\nFIM DA LISTA')