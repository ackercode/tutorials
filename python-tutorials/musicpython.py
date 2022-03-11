import pygame

pygame.mixer.init()
pygame.mixer.music.load("musica.mp3") #nome do seu arquivo de musica
pygame.mixer.music.play()

# para parar o arquivo rodando digite CTRL+C
# ou crie essa function para = input('Digite alguma letra')
