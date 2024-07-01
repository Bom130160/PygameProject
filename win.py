# Отображение результатов раунда

from const import *

def draw_win(objects: list, win_flag: bool, score_ship, score_sub) -> tuple:
	fin_win_flag = False
	for ob in objects:
		if win_flag:
			if ob.type == 'vessel':
				if ob.vessel_type == 'ship':
					score_sub += 1
				else:
					score_ship += 1
				if score_sub == 5 or score_ship == 5:
					fin_win_flag = True
					if score_ship != score_sub:
						pygame.draw.rect(window, ob.color, (160, 175, 470, 260))
						font = pygame.font.Font("fonts/JOKERMAN.TTF", 48)

						if ob.vessel_type == 'ship':
							text = font.render('Winner: Computer', True, 'red')
						else:
							text = font.render('Winner: Player', True, 'red')
						rect = text.get_rect(center=(400, 304))
						window.blit(text,rect)
						score_sub = score_ship = 0

				else:
					font = pygame.font.Font(None, 48)
					text1 = font.render(f'  Computer: {score_sub}',	True,'black')
					text2 = font.render(f'Player:    {score_ship}',True, 'black')
					pygame.draw.rect(window, ob.color,(180, 175, 400, 250))
					rect1 = text1.get_rect(center=(370,	280))
					rect2 = text2.get_rect(center=(400,	320))

					window.blit(text1, rect1)
					window.blit(text2, rect2)

	return score_sub, score_ship, fin_win_flag
