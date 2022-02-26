n1 = float(input('Digite uma distância em metros: '))
mm = n1 * 1000
cm = n1 * 100
dm = n1 * 10
dam = n1 / 10
hm = n1 / 100
km = n1 / 1000
print(f'A medida de {n1}m corresponde a '
      f'\n{cm:} CM '
      f'\n{mm} MM'
      f'\n{dm} Dm'
      f'\n{dam} Dam'
      f'\n{hm} Hm'
      f'\n{km} Km')

