numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
            'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete',
            'dezoito', 'dezenove', 'vinte')
while True:
    n1 = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n1 <= 20:
        break
    n1 = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {numeros[n1]}')
