import pygame
import sys

pygame.init()

pygame.display.set_caption('2d_Game')

screen = pygame.display.set_mode((1280,720))


clock=pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    
    pygame.display.update()
    clock.tick(60)
