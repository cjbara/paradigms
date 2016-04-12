import sys
import os
import math
import pygame
from Laser import *
from pygame.locals import *

class DeathStar(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		#initialize the object
		pygame.sprite.Sprite.__init__(self)
		self.gs = gs
		pygame.mixer.init()
		self.laserNoise = pygame.mixer.Sound(os.path.join("media", "screammachine.wav"))

		#Create the original image and the rectangle it is in
		self.orig_image = pygame.image.load("media/deathstar.png")
		self.rect = self.orig_image.get_rect()
	
		#Movement length per step
		self.delta = 5
		
		#The deathstar is not currently shooting
		self.shooting = False

		#Create all images and store them in the self.rotated_images array
		self.image = self.orig_image
		self.rotated_images = []
		self.angle = 0
		for x in range(0,360):
			self.rotated_images.append(self.rot_center(self.orig_image, x))

	def handleInput(self):
		for event in pygame.event.get():
			#if the user clicks the x
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit(0)
			#if the user presses an arrow key
			elif event.type == pygame.KEYDOWN:
				if event.key == K_LEFT:
					self.move('left')
				elif event.key == K_RIGHT:
					self.move('right')
				elif event.key == K_UP:
					self.move('up')
				elif event.key == K_DOWN:
					self.move('down')
			#mouse down
			elif event.type == pygame.MOUSEBUTTONDOWN:
				self.changeLaser(True)
			#mouse up
			elif event.type == pygame.MOUSEBUTTONUP:
				self.changeLaser(False)

	def move(self, direction):
		"""Function to handle movement from input"""
		(x, y) = self.rect.center
		if direction == 'up':
			self.rect.center = (x, y - self.delta)
		elif direction == 'down':
			self.rect.center = (x, y + self.delta)
		elif direction == 'left':
			self.rect.center = (x - self.delta, y)
		elif direction == 'right':
			self.rect.center = (x + self.delta, y)

	def tick(self):
		(mx, my) = pygame.mouse.get_pos()
		(cx, cy) = self.rect.center

		#if self.shooting is true, add a new laser to the object pool
		if self.shooting == True:
			self.gs.lasers.append(Laser(self.gs))
			self.laserNoise.play()
		
		#calculate the new angle
		self.angle = math.atan2(mx - cx, my - cy)
		index = int(math.floor(self.angle * 180 / math.pi + 180) + 42)
		if index >= 360:
			index = index - 360
		self.image = self.rotated_images[index]

	def changeLaser(self, boolean):
		self.shooting = boolean

	def rot_center(self, image, angle):
		"""rotate an image while keeping its center and size"""
		orig_rect = image.get_rect()
		rot_image = pygame.transform.rotate(image, angle)
		rot_rect = orig_rect.copy()
		rot_rect.center = rot_image.get_rect().center
		rot_image = rot_image.subsurface(rot_rect).copy()
		return rot_image
