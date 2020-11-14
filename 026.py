peso = float(input('Digite um peso: '))

if peso > 50:
    excedido = ((peso - 50)*4)
    print('O peso excedeu o limite, voce soferá uma multa de {} reias'.format(excedido))
elif peso == 50:
    print('O peso passou raspando')
else:
    print('O peso está abaixo do valor estabelecido')
