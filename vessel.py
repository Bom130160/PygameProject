# Класс Судно

from const import *
from bullet import Bullet

class Vessel:
	def __init__(self, vessel_type: str, color: str, px: int, py: int, direct: int, keylist: tuple, img, objects: list,
				 score_ship: int, score_sub: int) -> None:

		objects.append(self)
		self.type = 'vessel'
		self.color = color
		self.img = img
		self.vessel_type = vessel_type
		self.rect = pygame.Rect(px, py, TILE, TILE)
		self.direct = direct
		self.moveSpeed = 2

		if vessel_type == 'ship':
			self.score = score_ship
		else:
			self.score = score_sub

		self.shotTimer = 0
		self.shotDelay = 60
		self.bulletSpeed = 5

		self.keyLEFT = keylist[0]
		self.keyRIGHT = keylist[1]
		self.keySHOT = keylist[2]
		self.image = img
		self.image = pygame.transform.rotate(self.img, -self.direct * 90)
		self.image = pygame.transform.flip(self.image, False, True)
		self.rect = self.image.get_rect(center=self.rect.center)

	def update(self, keys: list, objects: list, bullets: list) -> None:
		self.image = pygame.transform.rotate(self.img, -self.direct * 90)
		if self.direct == 3:
			self.image = pygame.transform.flip(self.image, False, True)
		self.rect = self.image.get_rect(center=self.rect.center)
		oldx, oldy = self.rect.topleft
		if self.vessel_type == "sub": 		# горизонтальное движение судна от клавиш
			if keys[self.keyLEFT]:
				if 0 < oldx:
					self.rect.x -= self.moveSpeed
					self.direct = 3
			elif keys[self.keyRIGHT]:
				if oldx < WIDTH - 64:
					self.rect.x += self.moveSpeed
					self.direct = 1
		else:							# горизонтальное автономное движение подвоной лодки
			if self.direct == 3:
				if 0 < oldx:
					self.rect.x -= self.moveSpeed
					self.direct = 3
				else:
					self.direct = 1
			else:
				if oldx < WIDTH - 64:
					self.rect.x += self.moveSpeed
					self.direct = 1
				else:
					self.direct = 3

		for ob in objects:
			if ob != self and ob.type == 'sub' and self.rect.colliderect(ob.rect):
				self.rect.topleft = oldx, oldy

		if keys[self.keySHOT] and self.shotTimer == 0: # Стрельба подводной лодки по клавишие "пробел"
			if self.vessel_type == "sub":
				dy = DIRECTS[self.direct][1] * self.bulletSpeed
				Bullet(self, self.rect.centerx, self.rect.centery, 0, dy, self.color, bullets)
				self.shotTimer = self.shotDelay
		elif self.shotTimer == 0 and self.vessel_type == "ship":
				dy = - DIRECTS[self.direct][1] * self.bulletSpeed
				Bullet(self, self.rect.centerx,	self.rect.centery, 0, dy, self.color, bullets)
				self.shotTimer = self.shotDelay

		if self.shotTimer > 0:
			self.shotTimer -= 1

	def draw(self, window) -> None:						# прорисовка судна
		window.blit(self.image, self.rect)


	def damage(self, objects: list) -> None: 			# попадание снаряда в судно
		s = pygame.mixer.Sound('sounds/dead2.0.mp3')
		s.set_volume(0.7)
		s.play()
		sound = pygame.mixer.Sound('sounds/dead3.0.mp3')
		sound.set_volume(0.7)
		sound.play()

		objects.remove(self)
		win_flag = True
		return win_flag
