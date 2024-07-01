# Функция рисования стартовой заставки игры

import time
from draw_blocks import *
from rules import *
from const import *

def draw_intro(objects: list, first_start: bool, window): # objects - список объектов, first_start - флаг первого запуска
	score_sub = 0		# обнуление счета
	score_ship = 0

	font1 = pygame.font.Font("fonts/JOKERMAN.TTF", 60) 		# выбор шрифта

	if first_start:
		pygame.mixer.music.load('sounds/intro_music.mp3')	# музыка при первом входе в игру
	else:
		pygame.mixer.music.load('sounds/sea.mp3')			# музыка при последующих входах в игру
	pygame.mixer.music.play(-1)

	window.fill((45, 172, 227))								# заполнение фона заставки
	window.blit(yellow_submarine_img, (100, 0))				# рисунок подводной лодки на заставке
	pygame.display.update()

	start_flag = True					#
	start_button = False
	# игровой цикл заставки
	while start_flag:
		for e in pygame.event.get():		# анализ нажатых клавиш
			if e.type == pygame.QUIT:		# выход из приложения
				pygame.quit()
				sys.exit()

			elif e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN: 	# выход из цикла заставки
				start_flag = False

		if not start_button:
			window.fill((45, 172, 227))
			window.blit(yellow_submarine_img, (100, 0))
			text_start_game = font1.render('Start', True, (255, 221, 0))
			window.blit(text_start_game, (320, 483))

		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		pygame.display.update()

		if 100 < mouse[0] < 680 and 493 < mouse[1] < 563:		# подсвечиваем надпись Start
			start_button = True
			pygame.draw.rect(window, (190, 0, 0),(220, 493,	360, 70))
			text_start_game = font1.render('Start',	True, (255,	221, 0))
			window.blit(text_start_game, (320, 483))

			if click[0] == 1:
				start_flag = False
		else:
			start_button = False

		pygame.display.update()

	#  рисуем игровое поле и объекты
	window.blit(water_img, (0, 0))
	pygame.display.update()
	pygame.display.set_caption(f'Yellow Submarine       {score_ship} : {score_sub}      F1 - Help        Enter - Pause')
	draw_blocks(objects, score_ship, score_sub)
