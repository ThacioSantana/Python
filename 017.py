produto = str(input('Digite um nome de algum produto: '))
preço = float(input('Digite um valor para o produto: '))
quantidade_comprada = int(input('Digite a quantidade comprada: '))
total_pago = preço * quantidade_comprada

if quantidade_comprada <= 10:
    print('Pagará o total')
elif quantidade_comprada >= 11 or quantidade_comprada < 20:
    total_pago * (10/100)
    print('Pagará o preço com 10% de desconto')
elif quantidade_comprada >= 21 or quantidade_comprada < 50:
    total_pago * (20/100)
    print('Pagará o preço com 20% de desconto')
else:
    if quantidade_comprada > 50:
        total_pago * (25/100)
        print('Pagará o preço com 25% de desconto')
print('Obrigado pela compra e volte sempre!!!!!!')
