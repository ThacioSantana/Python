print('Bem Vindo a sua Calculadora particular!!!!!!!')
print('-----------------------------')
#adicionando valor as variaveis
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número, por favor: '))
#Criando a calculadora e a escolha das opções
print('Escola entre:\n [1]soma\n [2]subtração\n [3]multiplicação\n [4]divisão')
s1 = int(input('Digite um dos números acima: '))
if s1 == 1:
    print('Voce escolheu a soma e o resultado é: ',n1+n2)
elif s1 == 2:
    print('Voce escolheu a subtração e o resultado é: ',n1-n2)
elif s1 == 3:
    print('Voce escolheu a multiplicação e o resultado é: ',n1*n2)
elif s1 == 4:
    print('Voce escolheu a divisão e o resultado é:',n1/n2)
else:
    print('ERROR 404')
