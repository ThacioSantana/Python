import random
aluno1 = str(input('Digite um nome: '))
aluno2 = str(input('Digite um segundo nome: '))
aluno3 = str(input('Digite um terceiro nome: '))
aluno4 = str(input('Digite um quarto nome: '))
lista = [aluno1,aluno2,aluno3,aluno4]
escolhido = random.choice(lista)
print('O escolhido foi {}'.format(escolhido))