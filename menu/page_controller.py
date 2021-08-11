from menu.menu import Menu, Introduction_Menu
from game.game import Game


class Page_controller:
    """
    Used in start_menu.py to control the current menu or enter a level.
    """
    def __init__(self):
        self.level_state = [1, 0, 0, 0, 0]
        self.introduction_menu = Introduction_Menu()

    def choose_menu(self, response):
        if response == 'main menu':
            menu = Menu.MainMenu()
        elif response == 'level menu':
            menu = Menu.LevelMenu(self.level_state)
        elif response == 'introduction':
            menu = self.introduction_menu
        else:  # 防故障用(之後再移除)
            menu = Menu.MainMenu()
        menu.draw()
        return menu.update()

    def choose_level(self, response):
        if response == 'level_1':
            # 理論上遊戲會整個跑到結束才接著跑下一行
            quit_game, response, self.level_state[1] = Game('level_1').run()
        elif response == 'level_2':
            # 理論上遊戲會整個跑到結束才接著跑下一行
            quit_game, response, self.level_state[2] = Game('level_2').run()
        elif response == 'level_3':
            # 理論上遊戲會整個跑到結束才接著跑下一行
            quit_game, response, self.level_state[4] = Game('level_3').run()
        else:  # 防故障用(之後再移除)
            menu = Menu.LevelMenu(self.level_state)
            menu.draw()
            quit_game, response = menu.update()

        return quit_game, response

