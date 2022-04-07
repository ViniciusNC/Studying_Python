nome = str(input('Digite o seu nome completo: ')).strip().title()
nome1 = nome.split()
print(f'Existe a palavra Silva no seu nome? {"Silva" in nome1}')

