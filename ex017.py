import math
n1 = float(input('Digite o Cateto Adjacente do Triângulo: '))
n2 = float(input('Digite o Cateto Oposto do Triângulo: '))
hip = math.hypot(n2, n1)
print(f'A hipotenusa vai medir: {hip:.2f}')


