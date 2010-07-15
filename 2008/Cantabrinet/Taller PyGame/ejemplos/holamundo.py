#!/usr/bin/python

import pygame
import sys
from pygame.locals import *

# Inicializamos las bibliotecas de pygame
pygame.init()

# Creamos la ventana
screen = pygame.display.set_mode((180,40))
pygame.display.set_caption("Hola Mundo\n")
screen.fill((255,255,255))

# Creamos una superficie con el texto "Hola Mundo"
text = pygame.font.Font(None,40)
text_surface = text.render("Hola Mundo",True,(0,0,0))

# Copiamos la superficie de texto en la superficie de pantalla
screen.blit(text_surface,(0,0))

# Bucle de Eventos
while 1:
	# Actualizamos la pantalla
	pygame.display.update()

	# Captura de Eventos
	events = pygame.event.get()
	for e in events:
		# Cerrar la ventana
		if(e.type == QUIT):
			sys.exit()
		# Capturar las pulsaciones de teclado
		if(e.type == KEYDOWN):
			# Salir
			if(e.key == K_ESCAPE):
				sys.exit()
			# Pantalla completa
			if(e.key == K_f):
				pygame.display.toggle_fullscreen()
