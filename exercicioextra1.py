banca = float(input('Digite o valor da sua banca: '))
multiplicador = float(input('Digite o valor do multiplicador da aposta: x'))
print(f'SUA BANCA É DE: {banca} R$')
while True:
    aposta = float(input('Digite o valor apostado: '))
    if aposta > banca:
        banca = 0
        print('IMPOSSIVEL FAZER ESTA OPERAÇÃO')
        break
    banca -= aposta
    print(f'Sua banca agora é de: {banca:.2f}')
    win = str(input('Deu win a sua aposta? [S/N] ')).strip().upper()
    if win in 'S':
        multiplicador = multiplicador
        banca = banca + aposta * multiplicador
        print(f'Você ganhou {aposta*multiplicador}, agora você tem: {banca:.2f}')
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    multiplicador = float(input('Digite o valor do multiplicado da aposta: '))
    if continuar in 'N':
        break
print(f'Sua banca atual é de: {banca}')
