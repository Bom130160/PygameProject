import sys
from const import *

def rules() -> None:
	window.fill('black')
	font = pygame.font.Font(None, 60)
	text_sp = font.render('Space - Shot', True, (255, 255, 255))
	text_left = font.render('<-  - Left', True, (255, 255, 255))
	text_right = font.render('->  - Right', True, (255, 255, 255))
	text_pause = font.render('Enter  - Pause', True, (255, 255, 255))
	text_help = font. render('F1 - Help exit', True, (255, 255, 255))
	text_exit = font.render('Esc - Game exit', True, (255, 255, 255))


	window.blit(text_exit, (50, 550))
	window.blit(text_sp, (50, 50))
	window.blit(text_left, (50, 150))
	window.blit(text_right, (50, 250))
	window.blit(text_pause, (50, 350))
	window.blit(text_help, (50, 450))

