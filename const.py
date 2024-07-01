# Константы и загрузка рисунков

import pygame

WIDTH, HEIGHT = 800, 608  	# размер экрана
FPS = 60				 	# частота кадров
TILE = 32					# размер клетки

window = pygame.display.set_mode((WIDTH, HEIGHT))  # создание окна приложения
# загрузка рисунков
pygame.display.set_icon(pygame.image.load("images/military_ship.png"))
pygame.display.set_caption(f'Yellow summarine')
yellow_submarine_img = pygame.image.load('images/Yellow submarine.png')
water_img = pygame.image.load('images/water.png')
water_img = pygame.transform.scale(water_img, (WIDTH, HEIGHT))

imgBlocks = [pygame.image.load('images/block.png')]
imgShip = pygame.image.load('images/ship.png')
imgShip = pygame.transform.scale(imgShip, (64, 64))
imgSub = pygame.image.load('images/sub.png')

imgBangs = [pygame.image.load('images/bang1.png'),
			pygame.image.load('images/bang2.png'),
			pygame.image.load('images/bang3.png'),]

DIRECTS = [[0, -1],	[0,-1], [0, -1], [0, -1]]		# Список направлений


