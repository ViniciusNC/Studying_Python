nome = str(input('Digite seu nome completo: ')).strip()
dividido = nome.split()
print(f'Seu primeiro nome é: {dividido[0]}'
      f'\nSeu último nome é: {dividido[len(dividido)-1]}')
