print('Bem Vindo a Banco ATM')
restart = ('S')
chances = 3
balance = 999.12
while chances >= 0:
    pin == int(input('Por Favor digite a senha: '))
    if pin == (1234):
        print('Vocễ  digitou a senha correta')
        print('Por Favor precione 1 para seu balanço')
        print('Por Favor precione 2 para sua retirada')
        print('Por Favor precione 3 para entrar')
        print('Por Favor precione 4 para retornar o cartão')
        while restart not in ('n', 'NÃO', 'não', 'N'):
            print('Por Favor precione 1 para seu balanço')
            print('Por Favor precione 2 para sua retirada')
            print('Por Favor precione 3 para entrar')
            print('Por Favor precione 4 para retornar o cartão')
            opção == int(input('Qual a sua escolha?: '))
            
            if opção == 1:
                print('Seu Balanço é $',balance)
                break
            
            elif opção == 2:
                opção2 = ('S')
                retirada = float(input('Quanto voce vai retirar?
                                    10,20,40,60,80,100 for other enter 1:'))
        if retirada in [10,20,40,60,80,100]:
                        balance = balance - retirada
                        print('\nSeu balanço agora é $',balance)
                        restart = input('Voce gostaria de voltar?')
                                        if restart in('n','NÃO','N','não'):
                                            print('Obrigado')
                                            break
                    elif retirada != [10,20,40,60,80,100]:
                        print('ERROR 404, retire o cartão\n')
                        restart = ('S')
                    elif retirada == 1:
                        retirada = float(input('Por Favor retire a quantidade desejada:'))
                
                elif opção == 3:
                    pagar = float(input('Quanto voce gostaria de pagar? '))
                    balance = balance + pagar
                    print('\nSeu balanço agora é $',balance)
                    restart = input('Voce gostaria de voltar? ')
                    if restart in ('n','NÃO','N','não'):
                        print('Obrigado')
                        break
                elif opção == 4:
                    print('Por Favor espere enquanto seu cartão retorna')
                    print('Obrigado pelo seu serviços')
                    break
                else:
                    print('Por Favor digite sua senha,\n')
                    restart = ('S')
            