import pygame
from pygame.locals import *


#Set up pygame
pygame.init()

#Set up the window
windowSurface = pygame.display.set_mode((500, 400), 0 , 32)
pygame.display.set_caption('Hello World')

#Set up fonts
basicFont = pygame.font.SysFont(None, 48)

#Set up the text
text = basicFont.render('HELLO WORLD', True, (200,200,200))
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

#Draw the text onto the surface
windowSurface.blit(text,textRect)

#Draw the window onto the screen
pygame.display.update()




while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()