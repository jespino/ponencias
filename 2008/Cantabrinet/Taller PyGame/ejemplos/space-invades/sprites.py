#!/usr/bin/python

import pygame
from consts import *

# Clase invader
class Invader(pygame.sprite.Sprite):
	def __init__(self,x,y):
		# Inicializacion de la clase sprite
		pygame.sprite.Sprite.__init__(self)

		# Cargando la imagen del sprite
		self.image = pygame.image.load('data/invader.png')
		self.rect = self.image.get_rect(self.image)
		self.rect.centerx = x
		self.rect.centery = y
		self.speed = ALIEN_SPEED
		self.direction = "right" 

	def update(self):
		if self.direction == "right":
			self.rect = self.rect.move(self.speed,0)
		elif self.direction == "left":
			self.rect = self.rect.move(-self.speed,0)
		elif self.direction == "down":
			self.rect = self.rect.move(0,30)
		
class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('data/player.png')

		self.rect = self.image.get_rect(self.image)

		self.speed = PLAYER_SPEED
		self.rect.centerx = SCREEN_WIDTH/2
		self.rect.bottom = SCREEN_HEIGHT

	def move(self,direction):
		if direction == "right":
			self.rect = self.rect.move(self.speed,0)
		elif direction == "left":
			self.rect = self.rect.move(-self.speed,0)

class PlayerShot(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('data/player_shot.png')
		
		self.rect = self.image.get_rect(self.image)

		self.speed = PLAYER_SHOT_SPEED
		self.rect.centerx = x
		self.rect.centery = y

	def update(self):
		self.rect = self.rect.move(0,-self.speed)
		if self.rect.top <= 0:
			self.kill()

class AlienShot(pygame.sprite.Sprite):
	def __init__(self,x,y,bottom):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('data/alien_shot.png')
		
		self.rect = self.image.get_rect(self.image)

		self.speed = ALIEN_SHOT_SPEED
		self.rect.centerx = x
		self.rect.centery = y
		self.bottom = bottom

	def update(self):
		self.rect = self.rect.move(0,self.speed)
		if self.rect.top >= self.bottom:
			self.kill()

class FinishLabel(pygame.sprite.Sprite):
	def __init__(self,text):
		pygame.sprite.Sprite.__init__(self)
		font = pygame.font.Font(None,50)
		self.image = font.render(text,True,(255,255,255))
		self.rect = self.image.get_rect()
		self.rect.centerx = 320
		self.rect.centery = 240
	def draw(self,screen):
		screen.blit(self.image,(self.rect.left,self.rect.top))
