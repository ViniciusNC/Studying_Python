nome = str(input('Digite seu nome completo: ')).strip()
dividido = nome.split()
print(f'Seu nome comple em Minúsculo fica: {nome.lower()}'
      f'\nSeu nome completo em Maiúsculo fica: {nome.upper()}'
      f'\nA quantidade de letras que tem seu nome sem espaços: {len("".join(dividido))}'
      f'\nA quantidade de letras do seu primeiro nome: {len(dividido[0])}')
