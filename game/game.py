import pygame
from game.controller import GameControl
from game.model import GameModel
from game.view import GameView
from settings import FPS


class Game:
    def __init__(self, level):
        self.game_model = GameModel(level)  # core of the game (database, game logic...)
        self.game_view = GameView()  # render everything
        self.game_control = GameControl(self.game_model, self.game_view)  # deal with the game flow and user request

    def run(self):
        # initialization
        pygame.init()
        quit_game = False
        game_over = False
        jump_page = False
        but_response = None
        while not quit_game:
            pygame.time.Clock().tick(FPS)  # control the frame rate
            if not game_over:
                # for game start
                self.game_control.receive_user_input()  # receive user input
                self.game_control.update_model()  # update the model
                self.game_control.update_view()  # update the view
                pygame.display.update()
                quit_game = self.game_control.quit_game
                game_over = self.game_control.game_over
            else:
                # for game over
                self.game_control.update_game_over_view()
                pygame.display.update()
                while not jump_page:
                    self.game_control.receive_user_input()  # receive user input
                    self.game_control.update_game_over_model()
                    but_response, jump_page = self.game_control.jump_page_data  # but_response: 準備跳去的頁面
                    quit_game = self.game_control.quit_game
                break
        return quit_game, but_response, self.game_control.unlock_next_level

