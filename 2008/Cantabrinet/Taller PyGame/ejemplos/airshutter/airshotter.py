import sys
import pygame
import assprites
import asconsts
import random
import time
import psyco
psyco.full()
from pygame.locals import *
from asconsts import *

pygame.init()
random.seed(time.time())

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
#pygame.display.caption("Air Shotter")

background = pygame.Surface(screen.get_size()).convert()
background.fill(BLACK)

birds = pygame.sprite.RenderUpdates()
planes = pygame.sprite.RenderUpdates()
player_shots = pygame.sprite.RenderUpdates()
birds_shots = pygame.sprite.RenderUpdates()
explosions = pygame.sprite.RenderUpdates()
scores = pygame.sprite.RenderUpdates()

player = assprites.Plane()

score = assprites.Score()

scores.add(score)

planes.add(player)

gameover_text = assprites.GameOver()

while 1:
	pygame.time.wait(40)
	for event in pygame.event.get():
		if event.type==QUIT:
			sys.exit()
		elif event.type==KEYDOWN and event.key==K_ESCAPE:
			sys.exit()
		elif event.type==KEYDOWN and event.key==K_SPACE and len(planes)>0:
			shot = assprites.Shot((player.rect.right,player.rect.centery),(SHOT_SPEED,0))
			player_shots.add(shot)

	# Moving de Plane
	pressed = pygame.key.get_pressed()
	if pressed[273]:
		player.move(0,-PLANE_SPEED);
	if pressed[274]:
		player.move(0,PLANE_SPEED);
	if pressed[275]:
		player.move(PLANE_SPEED,0);
	if pressed[276]:
		player.move(-PLANE_SPEED,0);

	if random.randrange(100)>95:
		bird = assprites.Bird()
		birds.add(bird)

	for bird in birds:
		if random.randrange(100)>90:
			birds_shots.add(assprites.Shot((bird.rect.left,bird.rect.centery),(-SHOT_SPEED,0)))
			
		

	player_shots.update()
	planes.update()
	birds.update()
	explosions.update()
	scores.update()
	birds_shots.update()

	collides = pygame.sprite.groupcollide(player_shots,birds,True,True)
	for bird in collides.values():
		explosions.add(assprites.Explode(bird[0].rect.left,bird[0].rect.centery))
		score.inc()

	collides = pygame.sprite.groupcollide(birds,planes,True,True)
	for touched_player in collides.values():
		explosions.add(assprites.Explode(touched_player[0].rect.right,touched_player[0].rect.centery))

	collides = pygame.sprite.groupcollide(birds_shots,planes,True,True)
	for touched_player in collides.values():
		explosions.add(assprites.Explode(touched_player[0].rect.right,touched_player[0].rect.centery))


	screen.blit(background,(0,0))
	explosions.draw(screen)
	scores.draw(screen)
	birds.draw(screen)
	birds_shots.draw(screen)
	planes.draw(screen)
	player_shots.draw(screen)
	if len(planes)==0 and len(explosions)==0:
		screen.blit(gameover_text.image,gameover_text.rect)

	pygame.display.flip()
