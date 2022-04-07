frase = str(input('Digite sua frase: ')).strip().upper()
palavras = frase.split()
juntas = ''.join(palavras)
inverso = ''
for letra in range(len(juntas) - 1, -1, -1):
    inverso += juntas[letra]
if inverso == juntas:
    print('A FRASE É UM PALÍNDROMO')
else:
    print('A frase não é uma palíndromo')
