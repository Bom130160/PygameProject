# Класс взрыв

from const import *

class Bang:
	def __init__(self, px: int, py: int, objects: list, typ: str) -> None:
		objects.append(self)
		self.type = 'bang'
		self.other_type = typ
		self.px, self.py = px, py
		self.frame = 0

	def update(self, keys: list, objects: list, bullets: list) -> None:
		if self.frame == 0:
			if self.other_type == 'block':
				s = pygame.mixer.Sound('sounds/shot_block2.0.mp3')
				s.set_volume(0.3)
				s.play()
				sound = pygame.mixer.Sound('sounds/shot_block.mp3')
				sound.set_volume(0.9)
				sound.play()
		self.frame += 0.4
		if self.frame >= 3:
			objects.remove(self)
		elif self.px == (0 or WIDTH) or self.py == (0 or HEIGHT):
			objects.remove(self)

	def draw(self, window) -> None:
		image = imgBangs[int(self.frame)]
		rect = image.get_rect(center=(self.px, self.py))
		window.blit(image, rect)
