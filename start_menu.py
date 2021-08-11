import pygame
from menu.intro import Intro
from menu.page_controller import Page_controller
from settings import WIN_WIDTH, WIN_HEIGHT, FPS

pygame.init()
pygame.mixer.init()


class StartMenu:
    """the menu in front of the game start, including the opening"""
    def __init__(self):
        # win
        self.menu_win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        # set start page as intro
        self.page = 'intro'
        self.intro = Intro()
        self.page_controller = Page_controller()

    def menu_run(self):
        quit_game = False
        clock = pygame.time.Clock()
        pygame.display.set_caption("Cat-to-vid")

        while not quit_game:
            clock.tick(FPS)
            if self.page == 'intro':  # 開場動畫 (強制看完 LOGO，不准關XD)
                self.page = self.intro.fade_effect()
            elif self.page.startswith('level'):
                quit_game, self.page = self.page_controller.choose_level(self.page)  # 關卡選擇
            else:
                quit_game, self.page = self.page_controller.choose_menu(self.page)  # 主頁面選單

        pygame.quit()

