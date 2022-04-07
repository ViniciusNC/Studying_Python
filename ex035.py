r1 = float(input('Digite o lado A do triângulo: '))
r2 = float(input('Digite o lado B do triângulo: '))
r3 = float(input('Digite o lado C do triângulo: '))
if r1+r2 > r3 and r1+r3 > r2 and r2+r3 > r1:
    print('É possível fazer um triângulo')
else:
    print('Não é possivel fazer um triângulo')
