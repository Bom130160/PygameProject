# Класс Снаряд

from bang import *

class Bullet:
	def __init__(self, parent, px: int, py: int, dx: int, dy: int, color: str, bullets: list) -> None:
		s = pygame.mixer.Sound('sounds/vessel_shot.mp3')
		s.set_volume(0.4)
		s.play()
		bullets.append(self)
		self.parent = parent
		self.px, self.py = px, py
		self.dx, self.dy = dx, dy
		self.color = color
		self.count = 16
		self.flag = True

	def update(self,objects: list, bullets: list) -> bool:
		self.px += self.dx
		self.py += self.dy

		if self.px < 0 or self.px > WIDTH or self.py < 0 or self.py > HEIGHT:
			bullets.remove(self)
		else:
			for ob in objects:
				if ob != self.parent and ob.type != 'bang':
					if ob.rect.collidepoint(self.px, self.py):			# снаряд попал в объект
						if ob.type == 'block':
							objects.remove(ob)
						bullets.remove(self)
						Bang(self.px, self.py, objects, ob.type).draw(window)
						if ob.type == 'vessel':
							return ob.damage(objects)
						return False

	def draw(self, window) -> None:
		if self.count != 0:
			pygame.draw.circle(window,(255,	165, 0), (self.px + 2 * self.dx, self.py + 2 * self.dy), self.count)
			self.count -= 2
		if not self.flag:
			pygame.draw.circle(window, (255, 165,0), (self.px - self.dx, self.py - self.dy), 3)
			pygame.draw.circle(window,(255, 215, 0), (self.px - 2 * self.dx, self.py - 2 * self.dy), 2)
		pygame.draw.circle(window, self.color, (self.px, self.py), 4)
		self.flag = False
