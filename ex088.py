jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: ')).upper().strip()
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
total = 0
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols eles fez na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('*='*30)
print(jogador)
print('*='*30)
for k, v in jogador.items():
    print(f'{k} = {v}')
print('*='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador["gols"]):
    print(f'    --> Na partida {i}, fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')