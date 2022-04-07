from math import cos, sin, tan, radians
n1 = float(input('Digite um ângulo: '))
cosseno = cos(radians(n1))
seno = sin(radians(n1))
tan = tan(radians(n1))
print(f'A Tangente do Ângulo que digitou é: {tan:.2f}'
      f'\nO Seno do Ângulo que digitou é: {seno:.2}'
      f'\nO Cosseno do Ângulo que digitou é: {cosseno:.2f}')

