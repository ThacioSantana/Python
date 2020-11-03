import math
angulo = float(input('Digite um angulo: '))
n1 = math.sin(math.radians(angulo))
n2 = math.cos(math.radians(angulo))
n3 = math.tan(math.radians(angulo))
print('Os resultados do angulo {} são {:.2f} {:.2f} {:.2f}'.format(angulo,n1,n2,n3))