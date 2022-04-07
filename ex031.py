distancia = float(input('Digite a distância da viagem: '))
curta = distancia*0.50
longa = distancia*0.45
if distancia > 200:
    print(f'A viagem teve 0,05R$ de desconto pois será mais de 200KM: {longa}R$')
else:
    print(f'A viagem ficou por: {curta}R$')

