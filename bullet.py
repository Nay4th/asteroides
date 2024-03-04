import pygame, math
from pygame.sprite import Sprite
from pygame.locals import*
class Bullet(Sprite):
    def __init__(self, pos, angle, vel, cont):
        Sprite.__init__(self)
        self.vel=True
        self.alcane=25
        self.contenedor=cont
        self.image=pygame.image.load("Imagenes/bala.png")
        self.rect=self.imag.get_rect()
        self.rect.move_ip(pos[0], pos[1])
        self.angulo=angle
    def update(self):
        self.alcance-=1
        self.vel[0]+=math.cos(math.radians((self.angulo)))
