def area(a, b):
    are = a * b
    print(f'A a area de um terreno {a}x{b} é de {are}m')


print('CONTROLE DE TERRENO')
area(a=float(input(f'LARGURA(m): ')), b=float(input(f'COMPRIMENTO(m): ')))
