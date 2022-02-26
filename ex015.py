dias = float(input('Quantos dias alugado? '))
km = float(input('Quantos KM rodados? '))
valor = dias*60 + km*0.15
print(f'O total a pagar é de R${valor:.2f}')


