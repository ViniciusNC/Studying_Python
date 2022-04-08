s = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()[0]
while s not in 'MF':
        s = str(input('POR FAVOR DIGITE M OU F: ')).strip().upper()[0]
print('Parabéns você conseguiu')