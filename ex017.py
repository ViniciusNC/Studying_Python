from math import sqrt
n1 = float(input('Digite o Cateto Adjacente do Triângulo: '))
n2 = float(input('Digite o Cateto Oposto do Triângulo: '))
catetoadja = pow(n1, 2)
catetoopos = pow(n2, 2)
hipotenusa = sqrt((catetoadja + catetoopos))
print(f'O comprimento da hipotenusa é: {hipotenusa:.2f}')


