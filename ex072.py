palavras = 'feijao', 'arroz', 'pedra', 'tabuleiro', 'carta', 'pessoa', 'samurai', 'ocidente'
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')