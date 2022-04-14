cont = soma = numero = 0
while True:
    numero = int(input('Digite um número [999 para parar] '))
    if numero == 999:
        break
    cont += 1
    soma += numero
print(f'Você digitou {cont} numeros e a soma entre eles foi {soma}')