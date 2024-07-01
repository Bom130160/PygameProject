# Модуль игры

from draw_intro import *
from win import draw_win
from const import *
from rules import rules

def game() -> None:
	objects = []
	bullets = []
	win_flag = False
	score_ship = 0
	score_sub = 0

	draw_intro(objects, True, window) 	#вызов функции рисования заставки

	pygame.mixer.music.load('sounds/start.mp3')		# старт игры
	pygame.mixer.music.set_volume(0.6)
	pygame.mixer.music.play()

	paused = False
	play = True

	clock = pygame.time.Clock()

	# основной игровой цикл
	while play:
		window.blit(water_img, (0, 0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:		# Выход из приложения
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE: # ESC выход из игры в заставку
					if not paused:
						time.sleep(0.5)
						pygame.mixer.music.load('sounds/finish.mp3')
						pygame.mixer.music.set_volume(0.9)
						pygame.mixer.music.play()
						time.sleep(6)
						bullets = []
						objects = []
						pygame.mixer.music.stop()
						draw_intro(objects, False, window)

				elif event.key == pygame.K_RETURN or event.key == pygame.K_F1: 	# ENTER отображение счета и пауза
					if event.key == pygame.K_RETURN:
						f = pygame.font.Font(None, 48,)
						text1 = f.render(f'Computer: {score_sub}', True, 'black')
						text2 = f.render(f'Player: {score_ship}', True, 'black')
						text3 = f.render('Pause', True, 'black')
						pygame.draw.rect(window, (230, 230, 230), (260, 175, 250, 250))
						r1 = text1.get_rect(center=(370, 300))
						r2 = text2.get_rect(center=(400, 360))
						r3 = text3.get_rect(center=(390, 200))
						window.blit(text1, r1)
						window.blit(text2, r2)
						window.blit(text3,r3)
					else:
						rules()
					pygame.display.update()
					if paused:
						paused = False
					else:
						paused = True

		if not paused:
			keys = pygame.key.get_pressed()
			for bullet in bullets:
				win_flag = bullet.update(objects, bullets) # обновление флага победы в раунде
				if win_flag: break
			for obj in objects:
				obj.update(keys, objects, bullets) # работа с объектами
			for bullet in bullets:
				bullet.draw(window)  # прорисовка снарядов
			for obj in objects:
				obj.draw(window)	# прорисовка объектов

			# вывод на экран счета, если раунд или игра закончилась
			score_sub, score_ship, fin_win_flag = draw_win(objects, win_flag, score_ship, score_sub)
			pygame.display.update()

		clock.tick(FPS)
		if not pygame.mixer.music.get_busy():
			pygame.mixer.music.load('sounds/background_music.mp3')
			pygame.mixer.music.set_volume(0.3)
			pygame.mixer.music.play(-1)

		if win_flag:			# разбор ситуации после выигрыша раунда
			bullets = []
			objects = []
			pygame.mixer.music.load('sounds/finish1.mp3')
			pygame.mixer.music.set_volume(0.9)
			pygame.mixer.music.play()
			time.sleep(5)
			pygame.mixer.music.stop()
			win_flag = False
			pygame.display.set_caption(f'Yellow submarine {score_sub} : {score_ship}')

			if fin_win_flag: 	# завершение игры и переход к заставке
				paused = False
				time.sleep(0.5)
				draw_intro(objects, False, window)

			else:				# завершение очередного раунда игры и переход к новому раунду
				draw_blocks(objects, score_sub, score_sub)
