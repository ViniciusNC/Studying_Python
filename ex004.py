n = input('Digite algo ')
b = type(n)
print(f'Você digitou um número que tem o seguinte tipo primitivo {b}')
print('Caso o resultado a seguir for false ele não é Alfa Númerico ',n.isalnum())
print('Caso o resultado a seguir for false ele não faz parte do Alfabeto ',n.isalpha())
print('Caso o resultado a seguir for false ele não é um Número ',n.isnumeric())
print('Caso o resultado a seguir for false ele não está em Maiúsculo',n.isupper())
print('Caso o resultado a seguir for false ele não está em Minúsculo',n.islower())