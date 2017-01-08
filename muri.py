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

def save_image(screen):
	pygame.image.save(screen, "screen.bmp")

while True:
	clock.tick(30)
	keys = pygame.key.get_pressed()
	if keys[K_ESCAPE]: sys.exit()
	if keys[K_s]: cursor_y += 1
	if keys[K_r]: cursor_y -= 1
	if keys[K_a]: cursor_x -= 1
	if keys[K_t]: cursor_x += 1
	if keys[K_q]: save_image(screen)
	if keys[K_w]: cursor_size += 1
	if keys[K_f]: cursor_size -= 1

	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	screen.fill((0, 0, 0))
	pygame.draw.rect(screen,(255,0,0),(cursor_x, cursor_y, cursor_size, cursor_size))
	pygame.display.flip()	
