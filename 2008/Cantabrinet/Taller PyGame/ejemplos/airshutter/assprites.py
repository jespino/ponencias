import pygame
import random
import time
from asconsts import *

random.seed(time.time())

class Plane(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.speed = (0,0)
		#self.image = pygame.image.load("images/plane.png")
		self.image_front = pygame.image.load("images/helicopter/helicopter_front.png")
		self.image_back = pygame.image.load("images/helicopter/helicopter_back.png")
		self.image_normal = pygame.image.load("images/helicopter/helicopter_normal.png")
		self.image = self.image_normal
		self.rect = self.image.get_rect()
		self.rect.left = 11
		self.rect.centery = (SCREEN_HEIGHT/2)
	def move(self,x,y):
		if self.rect.left+x>0 and self.rect.right+x<SCREEN_WIDTH and self.rect.top+y>0 and self.rect.bottom+y<SCREEN_HEIGHT:
			self.rect = self.rect.move(x,y)
		if x>0:
			self.image = self.image_front
		elif x<0:
			self.image = self.image_back
		else:
			self.image = self.image_normal

class Shot(pygame.sprite.Sprite):
	def __init__(self,position,speed):
		pygame.sprite.Sprite.__init__(self)
		self.speed = speed
		self.image = pygame.image.load("images/shot.png")
		self.rect = self.image.get_rect()
		self.rect.centerx = position[0]
		self.rect.centery = position[1]
		sound = pygame.mixer.Sound("sounds/shut.wav")
		sound.play()

	def update(self):
		self.rect = self.rect.move(self.speed[0],self.speed[1])
		if self.rect.left>SCREEN_WIDTH or self.rect.right<0 or self.rect.top<0 or self.rect.bottom>SCREEN_HEIGHT:
			self.kill()

class Bird(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.speed = (-(random.randrange(3)+2),random.randrange(-3,3))
		self.image = pygame.image.load("images/bird.png")
		self.rect = self.image.get_rect()
		self.rect.right = SCREEN_WIDTH
		self.rect.centery = random.randrange(SCREEN_HEIGHT)

	def update(self):
		self.rect = self.rect.move(self.speed[0],self.speed[1])

class Explode(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.frames = []
		for count in range(8,23): 
			self.frames.insert(0,pygame.image.load("images/explode/explode-"+str(count)+".png"))

		self.image = pygame.image.load("images/explode/explode-0.png")
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.centery = y
		sound = pygame.mixer.Sound("sounds/explode.wav")
		sound.play()

	def update(self):
		if len(self.frames)>0:
			self.image = self.frames.pop()
		else:
			self.kill()

class Score(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.count = 0
		self.font = pygame.font.Font(pygame.font.get_default_font(),24)
		self.image = self.font.render(str(self.count),True,WHITE)
		self.rect = self.image.get_rect()
		self.rect.left = 10
		self.rect.top = 10

	def update(self):
		self.image = self.font.render("Score: "+str(self.count),True,WHITE)
		self.rect = self.image.get_rect()
		self.rect.left = 10
		self.rect.top = 10

	def inc(self):
		self.count+=10

class GameOver(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.font = pygame.font.Font(pygame.font.get_default_font(),48)
		self.image = self.font.render("Game Over",True,WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = SCREEN_WIDTH/2
		self.rect.centery = SCREEN_HEIGHT/2
