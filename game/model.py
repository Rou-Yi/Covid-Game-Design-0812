from enemy.enemy import EnemyGroup
from ally.ally import AllyGroup
from mana.mana import ManaGroup
from ally.ally_button_menu import Button_menu
from ending_page.ending_page import Ending_page
from game.user_request import *
from all_image import BACKGROUND_IMAGE


class GameModel:
    def __init__(self, level):
        # data
        self.bg_image = BACKGROUND_IMAGE
        self.__enemies = EnemyGroup()
        self.__allies = AllyGroup()
        self.__menu = Button_menu(level)
        self.__mana = ManaGroup(level)
        # selected item
        self.selected_button = None
        # game over variables
        self.unlock_next_level = False
        self.game_over = False
        self.game_over_win = False
        self.game_over_loss = False
        self.result = None
        # apply observer pattern
        self.subject = RequestSubject(self)
        self.generator = CatsGenerator(self.subject, level)
        #
        self.mana_value = self.__mana.mana_value

    def user_request(self, user_request: str):
        """ summon cats """
        self.subject.notify(user_request)

    def get_request(self, events: dict) -> str:
        """get keyboard response or button response"""
        # initial
        self.selected_button = None
        # mouse event
        if events["mouse position"] is not None:
            x, y = events["mouse position"]
            self.select(x, y)
            if self.selected_button is not None:
                return self.selected_button.response
            return "nothing"
        return "nothing"

    def select(self, mouse_x: int, mouse_y: int) -> None:
        """change the state of whether the items are selected"""
        # if the button is clicked, get the button response.
        for btn in self.__menu.get_buttons():
            if btn.clicked(mouse_x, mouse_y):
                self.selected_button = btn

    def allies_attack(self):
        """ 友軍執行攻擊 """
        for cats in self.__allies.get():
            cats.attack(self.__enemies)

    def allies_advance(self):
        """ 友軍執行移動、血量判斷 """
        self.game_over_loss = self.__allies.advance(self.__enemies)

    def enemies_campaign(self):
        """ 自動派出敵人 """
        self.__enemies.summon()
        self.__enemies.campaign()

    def enemies_attack(self):
        """ 敵人執行攻擊 """
        for virus in self.enemies.get():
            virus.attack(self.__allies)

    def enemies_advance(self, ):
        """ 敵人執行移動、血量判斷 """
        self.game_over_win = self.__enemies.advance(self.__allies)

    def mana_advance(self):
        """ 魔力條補充、魔力值更新 """
        """ 
        我真的沒辦法讓 self.__mana 裡面 mana 值
        直接在 user_request.py 的 CatsGenerator 裡被減掉 QQ
        Mana() 如果不留在這個檔案，給 View 畫圖時會卡住
        然後，檔案的__init__似乎沒辦法傳送 2 次 (self.__mana -> model.py -> user_request.py)
        """
        self.__mana.advance()
        self.mana_value = self.__mana.mana_value

    def game_over_advance(self):
        """ 當贏或輸成立時，結束遊戲 """
        if self.game_over_loss or self.game_over_win:
            self.game_over = True
            if self.game_over_loss:
                self.result = Ending_page.Loss()
            elif self.game_over_win:
                self.unlock_next_level = True
                self.result = Ending_page.Win()

    @property
    def enemies(self):
        return self.__enemies

    @property
    def allies(self):
        return self.__allies

    @property
    def menu(self):
        return self.__menu

    @property
    def mana(self):
        return self.__mana


