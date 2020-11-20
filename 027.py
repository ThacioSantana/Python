salario = float(input('Digite seu sálaraio: '))
ValorCasa = float(input('Digite o valor da casa: '))
QtAnos = int(input('Em quantos anos voce vai pagar a casa: '))
parcela = (ValorCasa / (QtAnos * 12))
print('Suas parcelas vão ser de {:.2f} R$'.format(parcela))

if parcela >= (salario * 0.3):
    print('Seu emprestimo foi negado')
else:
    print('Parabéns seu emprestimo foi aprovado')