salario = float(input('Por gentileza, digite seu sálario: R$ '))
aumento = salario*10/100
if salario >= 1250.00:
    print(f'Você recebeu um aumento de 10%: {salario+aumento}')
else:
    print(f'Você recebeu um aumento de 15%: {salario+(salario*15/100)}')


