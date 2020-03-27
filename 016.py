A = int(input('Digite um número: '))
B = int(input('Digite um número: '))
C = A

if A <= B:
    print('Vocễ acertou de primeira')
elif C == B:
    print('Você acertou de segunda, poderia ser melhor neh')
else: 
    A = B 
    B = C
    print('Os valores de',A,B)