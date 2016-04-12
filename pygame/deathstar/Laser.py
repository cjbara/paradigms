import sys
import os
import math
import pygame
from pygame.locals import *

class Laser(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		#initialize the object
		pygame.sprite.Sprite.__init__(self)
		self.gs = gs

		#Create the image
		self.image = pygame.image.load("media/laser.png")
		self.rect = self.image.get_rect()
		self.radius = self.rect.height / 2

		self.vel = 10
		(self.xpos, self.ypos) = self.gs.deathstar.rect.center
		self.xpos += 37*math.sin(self.gs.deathstar.angle)
		self.ypos += 37*math.cos(self.gs.deathstar.angle)
		self.rect.center = (self.xpos, self.ypos)
		self.xvel = self.vel * math.sin(self.gs.deathstar.angle)
		self.yvel = self.vel * math.cos(self.gs.deathstar.angle)

	def tick(self):
		self.xpos += self.xvel
		self.ypos += self.yvel
		self.rect.center = (self.xpos, self.ypos)

	def isOffScreen(self):
		if self.rect.right < 0 or self.rect.left > self.gs.width:
			if self.rect.bottom < 0 or self.rect.top > self.gs.height:
				return True
		return False