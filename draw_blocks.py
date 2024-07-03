# Функция создания экземпляров объектов (корабль, субмарина, блоков) на игровом поле

from vessel import Vessel
from blocks import *
from random import randint


def draw_blocks(objects: list, score_ship:int, score_sub:int) -> None:
	# Корабль
	Vessel('ship', 'cyan', 100,	40,	1, (0, 0, 0), imgShip, objects, score_ship, score_sub)
	# Подлодка
	Vessel('sub', 'yellow', 650, 500, 3,(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_SPACE), imgSub, objects,
			score_ship, score_sub)
	# Блоки
	for _ in range(30):
		while True:
			x = randint(0, WIDTH // TILE - 1) * TILE
			y = randint(4, (HEIGHT // TILE - 1) -5) * TILE
			rect = pygame.Rect(x, y, TILE, TILE)

			fined = False
			for ob in objects:
				if rect.colliderect(ob.rect):
					fined = True
			if not fined:
				break
		Block(x, y, objects, TILE)