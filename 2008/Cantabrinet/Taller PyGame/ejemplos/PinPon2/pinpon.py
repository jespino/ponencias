#!/usr/bin/python

import pygame
import sys
from pygame.locals import *
import random

# Inicializando pygame
pygame.init()

# Creando los objetos de juego
ball = pygame.image.load("data/ball.png")
ball_rect = ball.get_rect()
ball_rect.x = 100
ball_rect.y = 100
ball_speedx = 5
ball_speedy = 5
player1 = pygame.image.load("data/bar.png")
player1_rect = player1.get_rect()
player1_rect.centerx = 15
player1_rect.centery = 240
player2 = pygame.image.load("data/bar.png")
player2_rect = player1.get_rect()
player2_rect.centerx = 625
player2_rect.centery = 240

fuente = pygame.font.Font(None, 36)
puntos1=0
puntos2=0

# Creando la ventana principal (con titulo)
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('PinPon1')
pygame.display.set_icon(ball)
screen.fill((0,0,0))

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
		player1_rect = player1_rect.move(0,-8)
	elif key_state[K_DOWN]:
		player1_rect = player1_rect.move(0,8)
	elif key_state[K_q]:
		player2_rect = player2_rect.move(0,-8)
	elif key_state[K_a]:
		player2_rect = player2_rect.move(0,8)
	
	# Colision con la barra 1
	if ball_rect.left <= player1_rect.right and ball_rect.left >= player1_rect.left and ball_rect.top>= player1_rect.top and ball_rect.bottom<=player1_rect.bottom and ball_speedx<0: 
		ball_speedx = -ball_speedx
		puntos1+=10
		sound.play()
	
	# Colision con la barra 2
	if ball_rect.right >= player2_rect.left and ball_rect.right <= player2_rect.right and ball_rect.top>= player2_rect.top and ball_rect.bottom<=player2_rect.bottom and ball_speedx>0: 
		ball_speedx = -ball_speedx
		puntos2+=10
		sound.play()

	if ball_rect.bottom >= 480 or ball_rect.top <= 0:
		ball_speedy = -ball_speedy

	if ball_rect.left <= 0 or ball_rect.right >= 640:
		ball_speedy = 0
		ball_speedx = 0

	
	ball_rect = ball_rect.move(ball_speedx,ball_speedy)

	marcador1 = fuente.render("Player 1: "+str(puntos1),1,(255,255,255))
	marcador1_rect = marcador1.get_rect()
	marcador1_rect.top = 10
	marcador1_rect.left = 10
	marcador2 = fuente.render("Player 2: "+str(puntos2),1,(255,255,255))
	marcador2_rect = marcador2.get_rect()
	marcador2_rect.top = 10
	marcador2_rect.right = 630

	screen.fill((0,0,0))
	screen.blit(ball,ball_rect)
	screen.blit(player1,player1_rect)
	screen.blit(player2,player2_rect)
	screen.blit(marcador1,marcador1_rect)
	screen.blit(marcador2,marcador2_rect)

	if ball_speedx==0 and ball_speedy==0:
		gameover = fuente.render("Game Over",1,(255,255,255))
		gameover_rect = gameover.get_rect()
		gameover_rect.centerx = 320
		gameover_rect.centery = 240
		if ball_rect.right >= 640:
			winner = fuente.render("Player 1 wins",1,(255,255,255))
			winner_rect = winner.get_rect()
			winner_rect.centerx = 320
			winner_rect.top = gameover_rect.bottom+15
		else:
			winner = fuente.render("Player 2 wins",1,(255,255,255))
			winner_rect = winner.get_rect()
			winner_rect.centerx = 320
			winner_rect.top = gameover_rect.bottom+15
		screen.blit(gameover,gameover_rect)
		screen.blit(winner,winner_rect)
	

	pygame.display.flip()
