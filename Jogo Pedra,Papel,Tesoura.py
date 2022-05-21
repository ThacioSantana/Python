from random import randint
from time import sleep
itens = ("PEDRA", "PAPEL", "TESOURA")
maquina = randint(0, 2)
print('Bem Vindo ao jogo PEDRA,PAPEL,TESOURA')
print(('-=')*11)
print(('''Suas Escolhas são: \n[0]PEDRA \n[1]PAPEL \n[2]TESOURA'''))
jogador = int(input('Qual é sua escolha: '))
print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('TESOURA')
sleep(1)
if maquina == 0:
    if jogador == 0:
        print('Empatou com a maquina')
    elif jogador == 1:
        print('Jogador venceu')
    elif jogador == 2:
        print('A maquina venceu')
    else:
        print("ERROR 404")
elif maquina == 1:
    if jogador == 0:
        print('A maquina venceu')
    elif jogador == 1:
        print('Empatou com a maquina')
    elif jogador == 2:
        print('Jogador venceu')
    else:
        print("ERROR 404")
elif maquina == 2:
    if jogador == 0:
            print('Jogador venceu')
    elif jogador == 1:
        print('A maquina venceu')
    elif jogador == 2:
        print('Empatou com a maquina')
    else:
        print("ERROR 404")
print('-='*11)    