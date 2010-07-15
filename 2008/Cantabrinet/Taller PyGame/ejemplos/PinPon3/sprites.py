import pygame
from pygame.locals import *

# Sprite de barra para el jugador
class Bar(pygame.sprite.Sprite):
    def __init__(self,x):
	# Inicializacion del sprite
        pygame.sprite.Sprite.__init__(self)

	# Creacion de la imagen y el rectangulo del sprite
        self.image = pygame.image.load('data/bar.png')
        self.rect = self.image.get_rect(self.image)

	# Posicionamiento del rectangulo
        self.rect.centerx = x
        self.rect.centery = 30

	# Velocidad de la barra
        self.speed = 8

    # Movimiento del sprite
    def move(self,direction):
        if direction == "up":
            if self.rect.top-self.speed > 0:
              self.rect = self.rect.move(0,-self.speed)
        elif direction == "down":
            if self.rect.bottom+self.speed < 480:
              self.rect = self.rect.move(0,self.speed)

# Sprite para la bola
class Ball(pygame.sprite.Sprite):
    def __init__(self,x,y):
	# Inicializacion del sprite
        pygame.sprite.Sprite.__init__(self)

	# Creacion de la imagen y el rectangulo del sprite
        self.image = pygame.image.load('data/ball.png')
        self.rect = self.image.get_rect(self.image)

	# Posicionamiento del rectangulo
        self.rect.centerx = x
        self.rect.centery = y

	# Velocidad de la pelota
        self.speedx = 5
        self.speedy = 5

    # Bucle del sprite
    def update(self):
        if self.rect.bottom >= 480:
            self.speedy = -self.speedy
        elif self.rect.top <= 0:
            self.speedy = -self.speedy

        if self.rect.left <= 0:
            self.speedx = 0
            self.speedy = 0
        elif self.rect.right >= 640:
            self.speedx = 0
            self.speedy = 0

        self.rect = self.rect.move(self.speedx,self.speedy)

class Score(pygame.sprite.Sprite):
	def __init__(self,player_name,x):
		pygame.sprite.Sprite.__init__(self)
		self.score = 0
		self.name = player_name
		self.font = pygame.font.Font(None,30)
		self.image = self.font.render("Player "+self.name+": "+str(self.score),1,(255,255,255))
		self.rect = self.image.get_rect()
		self.rect.top = 15
		self.rect.centerx = x

	def inc(self):
		self.score+=10
		x=self.rect.centerx
		self.image = self.font.render("Player "+self.name+": "+str(self.score),1,(255,255,255))
		self.rect = self.image.get_rect()
		self.rect.top = 15
		self.rect.centerx = x

class GameOver(pygame.sprite.Sprite):
	def __init__(self,player_name):
		pygame.sprite.Sprite.__init__(self)
		self.score = 0
		font = pygame.font.Font(None,30)
		gameover_text = font.render("Game Over",1,(255,255,255))
		gameover_text_rect = gameover_text.get_rect()
		winner_text = font.render("Winner Player "+player_name,1,(255,255,255))
		winner_text_rect = winner_text.get_rect()
		self.image = pygame.Surface((max(gameover_text_rect.get_width(),winner_text_rect.get_width()),gameover_text_rect.get_height()+winner_text_rect.get_height()+15))

		gameover_text_rect.top = 0
		gameover_text_rect.centerx = self.image.get_rect().get_width()/2
		self.image.blit(gameover_text,gameover_text_rect)

		winner_text_rect.top = gameover_text_rect.bottom+15
		winner_text_rect.centerx = self.image.centerx
		self.image.blit(winner_text,winner_text_rect)

		self.rect.centerx = 320
		self.rect.centery = 240
