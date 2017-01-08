import pygame
from pygame.locals import *
import sys

pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MuRi")

clock = pygame.time.Clock()

cursor_x, cursor_y = 0,0
cursor_size = 2

while True:
	clock.tick(30)
	keys = pygame.key.get_pressed()
	if keys[K_ESCAPE]: sys.exit()
	if keys[K_j]: cursor_y += 1
	if keys[K_k]: cursor_y -= 1
	if keys[K_h]: cursor_x -= 1
	if keys[K_l]: cursor_x += 1

	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	screen.fill((0, 0, 0))
	pygame.draw.rect(screen,(255,0,0),(cursor_x, cursor_y, 2, 2))
	pygame.display.flip()	
