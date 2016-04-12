import sys
import os
import math
import pygame
from pygame.locals import *

class Explosion(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		#initialize the explosion
		pygame.sprite.Sprite.__init__(self)
		self.gs = gs

		self.framesPerImage = 2
		self.counter = 0
		self.index = 0
		self.completed = False

		self.explosions = []
		for x in range(0, 16):
			if x < 10:
				xstr = '0' + str(x)
			else:
				xstr = str(x)
			self.explosions.append(pygame.image.load('media/explosion/frames0'+xstr+'a.png'))

		self.image = self.explosions[self.index]
		self.rect = self.image.get_rect()
		self.rect.center = (self.gs.width * .6, self.gs.height * .8)

	def tick(self):
		self.counter += 1
		if self.counter >= self.framesPerImage:
			self.counter = 0
			self.index += 1
			if self.index <= 15:
				self.image = self.explosions[self.index]
			else:
				self.completed = True
