import sys
import os
import math
import pygame
from pygame.locals import *
from deathstar import *

class GameSpace(object):
	def __init__(self):
		#1 Initialize game space
		pygame.init()
		pygame.key.set_repeat(1,10)
		self.size = self.width, self.height = (640, 480)
		self.black = (0,0,0)
		self.screen = pygame.display.set_mode(self.size)
		self.clock = pygame.time.Clock()

		#2 Initialize game objects
		self.lasers = []
		self.deathstar = DeathStar(self)
		self.earth = Earth(self)
		self.explosion = Explosion(self)

	def main(self):
		#3 Start game loop
		while(1):
			#4 Tick regulation
			self.clock.tick(60)

			#5 Read User Input
			self.handleInput()

			#6 tick() all objects
			self.deathstar.tick()
			
			if self.earth.exploded == False:
				self.earth.tick()
			else:
				if self.explosion.completed == False:
					self.explosion.tick()
			for x in self.lasers:
				x.tick()

			#7 Update screen display
			self.screen.fill(self.black)
			self.screen.blit(self.deathstar.image, self.deathstar.rect)
			for x in self.lasers:
				self.screen.blit(x.image, x.rect)
			if self.earth.exploded == False:
				self.screen.blit(self.earth.image, self.earth.rect)
			else:
				if self.explosion.completed == False:
					self.screen.blit(self.explosion.image, self.explosion.rect)
			pygame.display.flip()

        def handleInput(self):
                for event in pygame.event.get():
                        #if the user clicks the x
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit(0)
                        #if the user presses an arrow key
                        elif event.type == pygame.KEYDOWN:
                                if event.key == K_LEFT:
                                        self.deathstar.move('left')
                                elif event.key == K_RIGHT:
                                        self.deathstar.move('right')
                                elif event.key == K_UP:
                                        self.deathstar.move('up')
                                elif event.key == K_DOWN:
                                        self.deathstar.move('down')
                                elif event.key == K_r:
                                        self.__init__()
                        #mouse down
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                                self.deathstar.changeLaser(True)
                        #mouse up
                        elif event.type == pygame.MOUSEBUTTONUP:
                                self.deathstar.changeLaser(False)

if __name__ == '__main__':
	game = GameSpace()
	game.main()
