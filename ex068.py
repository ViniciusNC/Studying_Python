times = ('São Paulo', 'Coritiba', 'Corinthians', 'Atlético-MG', 'Ceará-SC', 'Avaí', 'Cuiabá', 'Bragantino', 'Juventude',
         'Flamengo', 'Atlético-GO', 'Santos', 'Fluminense', 'Palmeiras', 'Fortaleza', 'América-MG', 'Botafogo',
         'Internacional', 'Goiás', 'Athletico - PR')
print(f'Os quatros primeiros colocados do Brasileirão 2022 são {times[0:5]}')
print('=-'*30)
print(f'Os quatros últimos colocados do Brasileirão 2022 são {times[16:]}')
print('=-'*30)
print(f'Times em oderdem alfabética {sorted(times)}')
print('=-'*30)
print(f'O Palmeiras está na posição {times.index("Palmeiras")+1}ª posição')
