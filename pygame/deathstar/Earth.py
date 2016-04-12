import sys
import os
import pygame
from pygame.locals import *

class Earth(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		#initialize the object
		pygame.sprite.Sprite.__init__(self)
		self.gs = gs
		self.damage = 100

		#get the image and put it in the bottom right corner
		self.orig_image = pygame.image.load("media/globe.png")
		self.damaged_image = pygame.image.load("media/globe_red100.png")
		self.empty_image = pygame.image.load("media/empty.png")
		self.rect = self.orig_image.get_rect()
		self.radius = self.rect.width / 2.1

		self.rect.center = (self.gs.width * .8, self.gs.height)
		self.image = self.orig_image
		self.exploded = False

	def tick(self):
		for x in self.gs.lasers:
			if pygame.sprite.collide_circle(self, x):
				self.gs.lasers.remove(x)
				self.damage -= 10
		
		if self.damage <= 30:
			self.image = self.damaged_image
		if self.damage <= 0:
			self.image = self.empty_image
			self.exploded = True
