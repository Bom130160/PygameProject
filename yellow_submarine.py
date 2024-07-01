# Главный модуль

from playing import *
import pygame

if __name__ == '__main__':
    pygame.init()       # инициализация pygame
    game()              # игра
    pygame.quit()       # завершение pygame
