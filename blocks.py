# Класс Блоки

from const import *

class Block:
	def __init__(self, px: int,	py: int, objects: list, size: int) -> None:
		objects.append(self)
		self.type = 'block'
		self.rect = pygame.Rect(px, py, size, size)

	def update(self, keys: list, objects: list, bullets: list) -> None:
		pass

	def draw(self, window) -> None:
		window.blit(imgBlocks[0], self.rect)

