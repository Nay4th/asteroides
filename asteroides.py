import pygame
from pygame.locals import *
import sys
from ship import *
size=width, height=800, 600
screen=pygame.display.set_mode(size)
def main():
    pygame.init()
    background_image=pygame.image.load("imagenes/espacio.jpg")
    background_rect=background_image.get_rect()
    pygame.display.set_caption("Asteroids")
    ship=Ship(size)
    while 1:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                sys.exit()
        ship.update()
        for bullet in ship.bullets:
            bullet.update()
            if bullet.alcance ==0:
                ship.bullet.remove(bullet)
            screen.blit(bullet.image, bullet.rect)
        screen.blit(background_image, background_rect)
        screen.blit(ship.imagen, ship.rect)
        pygame.display.update()
        pygame.time.delay(10)
if __name__=="__main__":
    main()