import pygame
 
nome = str(input('Digite um nome: '))
if nome == 'Thacio':
    pygame.init()
    pygame.mixer_music.load('ex1.mp3')
    pygame.mixer_music.play
    pygame.event.wait()
else:
    pygame.init()
    pygame.mixer_music.load('ex2.mp3')
    pygame.mixer_music.play
    pygame.event.wait()
    print('O seu nome é tão normal {}'.format(nome))
    

print('Olá, {} prazer em te conhecer!!! :)'.format(nome))