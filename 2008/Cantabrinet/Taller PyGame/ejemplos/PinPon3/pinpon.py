#!/usr/bin/python

import pygame
from pygame.locals import *
from sprites import *
import sys
import random

# Inicializando pygame
pygame.init()

# Creando la ventana principal (con titulo)
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('PinPon3')

# Creando y pegando el fondo de pantalla
screen.fill((0,0,0))
pygame.display.update()

# Creando los objetos de juego
ball = Ball(100,100)
player1 = Bar(15)
player2 = Bar(625)

score1 = Score("1",100)
score2 = Score("2",540)

# Anadiendolos al grupo
all = pygame.sprite.RenderUpdates((player1,player2,ball,score1,score2))

# Preparando el sonido
sound = pygame.mixer.Sound("data/ping.wav")

# Bucle de eventos
while 1:
	pygame.time.wait(40)
	# Lectura de eventos
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()
		if event.type == KEYDOWN and event.key == K_ESCAPE:
			sys.exit()
	
	# Comprobacion de las teclas pulsadas
	key_state = pygame.key.get_pressed()
	if key_state[K_UP]:
		player1.move("up")
	elif key_state[K_DOWN]:
		player1.move("down")
	elif key_state[K_q]:
		player2.move("up")
	elif key_state[K_a]:
		player2.move("down")
	
	# Colision con la barra 1
	if player1.rect.colliderect(ball.rect):
		ball.speedx = -ball.speedx
		sound.play()
		score1.inc()
	
	# Colision con la barra 2
	if player2.rect.colliderect(ball.rect):
		ball.speedx = -ball.speedx
		sound.play()
		score2.inc()

	if ball.rect.left<=0 or ball.rect.right>=640:
		ball.speedx=0

	if ball.speedx==0 and ball.rect.right>=640:
		gameover = GameOver("1")
		all.add(gameover)
	elif ball.speedx==0 and ball.rect.left<=0:
		gameover = GameOver("2")
		all.add(gameover)
	
	# Repintar la pantalla
	all.update()
	screen.fill((0,0,0))
	dirty = all.draw(screen)
	pygame.display.update(dirty)
