import sys
import os
import pygame
from pygame.locals import *

class DeathStar(pygame.sprite.Sprite):
    def __init__(self, gs=None):
        pygame.sprite.Sprite.__init__(self)
        self.gs = gs
        self.image = pygame.image.load("deathstar.png")
        self.rect = self.image.get_rect()
        self.orig_image = self.image

class GameSpace(object):
    def __init__(self):
        pygame.init()
        self.size = self.width, self.height = (640, 480)
        self.black = (0,0,0)

        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        
    def main(self):
        while(1):
            self.clock.tick(60)
            self.screen.fill(self.black)
            pygame.display.flip()

if __name__ == '__main__':
    game = GameSpace()
    game.main()
