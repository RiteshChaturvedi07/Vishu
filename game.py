# Scrolling Image--

# Basic code---
import pygame
import sys
pygame.init()

# Width and Height of Windows--
WSIZE = (0, 0)
windows=pygame.display.set_mode(WSIZE)

# Image Load--
bg=pygame.image.load('output-onlinepngtools.png')
bg_x=0
bg_y=0

# Title of Window--
pygame.display.set_caption('Scrolling BG')

# Color of Window--
WHITE=(255,255,255,255)

# Variable-
run=True
while run:
	#scrolling--
	bg_rel_x=bg_x % bg.get_rect().width #connecting image--
	
	windows.blit(bg,(bg_rel_x,0)) # draw the image in window--
	
	#condition--
	if bg_rel_x<1120:
		windows.blit(bg,(bg_rel_x-bg.get_rect().width,0))


	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False

	bg_y-=1 #start to move--
	pygame.display.update() # Its help every small change--

pygame.quit()
quit()