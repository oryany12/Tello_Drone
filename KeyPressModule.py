import pygame
from Global_params import *


def init():
    pygame.init()
    win = pygame.display.set_mode(GAME_PAD_SIZE)


def getKey(KeyName):
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(KeyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans
