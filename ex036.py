valor = float(input('Por gentileza, nos informe o valor da casa: R$ '))
salario = float(input('Por gentileza, nos informe o seu sálario: R$ '))
tempo = int(input('Por gentileza, nos informe em quantos anos você ira pagar: '))
tempo = tempo*12
valorM = valor / tempo
if valorM >= salario*30/100:
    print('Infelizmente não podemos dar continuidade com a compra do imóvel, pois o valor mensal excedeu 30% de seu sálario'
          '')
else:
    print('Parabéns você fez a compra da casa')
