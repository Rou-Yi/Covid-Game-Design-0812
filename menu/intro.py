import pygame
import os
from settings import WIN_WIDTH, WIN_HEIGHT, LV_BTN_WIDTH, LV_BTN_HEIGHT
from all_image import *


class Intro:  # 起始畫面
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.bg_image = MENU_BACKGROUND
        self.logo_image = LOGO_IMAGE
        self.alpha = 0
        self.fade = 'in'

    def fade_effect(self):
        surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA)
        surface.blit(self.bg_image, (0, 0))  # draw background
        surface.blit(self.logo_image, (237, 150))  # draw logo on a transparent surface
        if self.fade == 'in':
            if self.alpha < 255:
                self.alpha += 5
                surface.set_alpha(self.alpha)
                self.win.blit(surface, (0, 0))
                pygame.time.wait(2)
            else:
                self.fade = 'out'
                self.alpha = 200

        elif self.fade == 'out':
            self.win.blit(self.bg_image, (0, 0))  # every time draw a new background
            if self.alpha > 0:
                self.alpha -= 4
                surface.set_alpha(self.alpha)
                self.win.blit(surface, (0, 0))
            else:
                return 'main menu'
        pygame.display.flip()

        return 'intro'
