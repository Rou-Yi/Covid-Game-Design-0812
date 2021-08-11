from button import Button
from all_image import *


class Menu:
    """
    Construct the menu for the start of the level_2.
    """
    def __init__(self, button_list, response):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.bg_image = MENU_BACKGROUND
        self.__buttons = button_list
        self.button_response = response

    def draw(self):
        """
        Draw everything here.
        :return: None
        """
        # draw background
        self.win.blit(self.bg_image, (0, 0))
        self.win.blit(LOGO_IMAGE_small, (1017, 2))
        # draw button
        for but in self.__buttons:
            self.win.blit(but.image, but.rect)
        pygame.display.update()

    def update(self):
        """
        Update for quit event and click button.
        :return game_quit: whether quit the level_2.
                self.button_response: used for changing to next page.
        """
        quit_game = False
        # event loop
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = True
                return quit_game, self.button_response
            # player click action
            if event.type == pygame.MOUSEBUTTONDOWN:
                for btn in self.__buttons:
                    if btn.clicked(mouse_x, mouse_y):
                        self.button_response = btn.response
                        return quit_game, self.button_response
        return quit_game, self.button_response

    # 用繼承寫出三個主要頁面
    @classmethod
    def MainMenu(cls):  # 主頁面
        btn_list = [Button(LEVEL_BTN_IMAGE, "level menu", 400, 200),
                    Button(INTRO_BTN_IMAGE, "introduction", 800, 200),]
        main_menu = cls(btn_list, 'main menu')
        return main_menu

    @classmethod
    def LevelMenu(cls, level_state):  # 關卡選擇頁面
        btn_list = [Button(RETURN_IMAGE, "main menu", 75, 50)]
        Level_unlock = [Button(LV1_OP_BTN_IMAGE, "level_1", 200, 220),
                        Button(LV2_OP_BTN_IMAGE, "level_2", 400, 220),
                        Button(LV3_OP_BTN_IMAGE, "level_3", 600, 220),
                        Button(LV4_OP_BTN_IMAGE, "level_4", 800, 220),
                        Button(LV5_OP_BTN_IMAGE, "level_5", 1000, 220)]

        Level_locked = ["Level 1 has no locked problem.",
                        Button(LV2_CL_BTN_IMAGE, "level", 400, 220),
                        Button(LV3_CL_BTN_IMAGE, "level", 600, 220),
                        Button(LV4_CL_BTN_IMAGE, "level", 800, 220),
                        Button(LV5_CL_BTN_IMAGE, "level", 1000, 220)]

        # 如果關卡解鎖就放上解鎖圖按鈕
        btn_list.extend([Level_unlock[i] if level_state[i] else Level_locked[i] for i in range(5)])

        level_menu = cls(btn_list, 'level menu')
        return level_menu


class Introduction_Menu:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.surf = pygame.surface.Surface((WIN_WIDTH, WIN_HEIGHT*2))
        self.bg_image = MENU_BACKGROUND
        self.__pages = [INTRODUCE01, INTRODUCE02]
        self.__buttons = [Button(RETURN_IMAGE, "main menu", 75, 50)]
        self.button_response = 'introduction'
        self.scroll = 0

    def draw(self):
        """
        Draw everything here.
        :return: None
        """
        self.win.blit(self.bg_image, (0, 0))
        # draw page
        for i, page in enumerate(self.__pages):
            self.surf.blit(page, (0, WIN_HEIGHT*i))

    def update(self):
        """
        Update for quit event and click button.
        :return game_quit: whether quit the level_2.
                self.button_response: used for changing to next page.
        """
        quit_game = False
        while not quit_game:
            # event loop
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game = True
                    return quit_game, self.button_response
                # player click action
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for btn in self.__buttons:
                        if btn.clicked(mouse_x, mouse_y):
                            self.button_response = btn.response
                            return quit_game, self.button_response
                # 滾輪
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        self.scroll = min(self.scroll + 100, 0)
                    if event.button == 5:
                        self.scroll = max(self.scroll - 100, -WIN_HEIGHT)

            self.win.blit(self.surf, (0, self.scroll))
            # draw button
            for but in self.__buttons:
                self.win.blit(but.image, but.rect)
            self.win.blit(LOGO_IMAGE_small, (1017, 2))
            pygame.display.update()
