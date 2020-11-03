import math

co = float(input('Digite um número: '))
ca = float(input('Digite outro número: '))
hi = math.hypot(co,ca)
print('O comprimento do cateto oposto é {}, o do adjacente é {} e a hipotenusa é {:.2f}'.format(co,ca,hi))