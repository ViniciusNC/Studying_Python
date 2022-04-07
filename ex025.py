nome = str(input('Digite o nome da sua cidade: ')).strip().title()
dividido = nome.split()
print(f'A sua cidade começa com o nome Santo? {"Santo" in dividido[0]}')