#! /usr/bin/env python

import random, os.path

#import basic pygame modules
import sys
import pygame
from pygame.locals import *
from sprites import *
from consts import *

pygame.init()

# Configurando la ventana principal
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
icon = pygame.image.load(ICON_FILE)
pygame.display.set_icon(icon)
pygame.display.set_caption(WINDOW_TITLE)

# Creando el fondo
background = pygame.Surface(screen.get_size())
background.fill(BLACK)

# Creamos los grupos de widgets

aliens = pygame.sprite.RenderUpdates()
playershots = pygame.sprite.RenderUpdates()
alienshots = pygame.sprite.RenderUpdates()
players = pygame.sprite.RenderUpdates()

player = Player()
players.add(player)

for y in range(1,ALIEN_FILES):
	for x in range(1,ALIEN_COLUMNS):
    		invader = Invader(x*30,y*30)
		aliens.add(invader)

while 1:
	pygame.time.wait(60)
	
        for event in pygame.event.get():
        	if event.type == QUIT:
			sys.exit()
		elif (event.type == KEYDOWN and event.key == K_ESCAPE):
			sys.exit()
		elif (event.type == KEYDOWN and event.key == K_q):
			sys.exit()

       	keystate = pygame.key.get_pressed()
	if keystate[K_RIGHT]:
		player.move("right")
	elif keystate[K_LEFT]:
		player.move("left")
	if keystate[K_SPACE]:
		can_shot=True
		for shot in playershots:
			if shot.rect.bottom>player.rect.top-80:
				can_shot=False
		if can_shot:
			playershots.add(PlayerShot(player.rect.centerx,player.rect.top))

	if len(players)==0:
		text_sprite = FinishLabel("Game Over")
		screen.blit(background,(0,0))
		text_sprite.draw(screen)
		pygame.display.flip()
	elif len(aliens)==0:
		text_sprite = FinishLabel("You Win")
		screen.blit(background,(0,0))
		text_sprite.draw(screen)
		pygame.display.flip()
	else:
		action = ""
		direction = ""
		for alien in aliens:
			if alien.rect.left <= 20:
				action = "down"
				direction = "right"
			elif alien.rect.right >= screen.get_rect().right-20:
				action = "down"
				direction = "left"
			if int(random.random()*300)==1:
				alien_shot = AlienShot(alien.rect.centerx,alien.rect.bottom,screen.get_rect().bottom)
				alienshots.add(alien_shot)

		if action == "down":
			for alien in aliens:
				alien.direction = "down"
				alien.update()
				alien.speed = alien.speed+1
				alien.direction = direction
				alien.update()

        	# Detect collisions
        	if pygame.sprite.spritecollide(player, aliens, 1):
			player.kill()

        	if pygame.sprite.spritecollide(player, alienshots, 1):
			player.kill()

        	pygame.sprite.groupcollide(playershots, alienshots, 1, 1)

        	pygame.sprite.groupcollide(playershots, aliens, 1, 1)

		aliens.update()
        	players.update()
		alienshots.update()
		playershots.update()

        	#draw the scene
		screen.blit(background,(0,0))
		aliens.draw(screen)
        	players.draw(screen)
		alienshots.draw(screen)
		playershots.draw(screen)
        	pygame.display.flip()
