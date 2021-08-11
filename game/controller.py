import pygame


# controller
class GameControl:
    def __init__(self, game_model, game_view):
        self.model = game_model
        self.view = game_view
        self.events = {"game quit": False,
                       "mouse position": [0, 0],
                       }
        self.request = None  # response of user input

    def update_model(self):
        """update the model and the view here"""
        self.request = self.model.get_request(self.events)
        self.model.user_request(self.request)
        self.model.enemies_campaign()
        self.model.allies_attack()
        self.model.enemies_attack()
        self.model.allies_advance()
        self.model.enemies_advance()
        self.model.mana_advance()
        self.model.game_over_advance()

    def receive_user_input(self):
        """receive user input from the events"""
        # event initialization
        self.events = {"game quit": False,
                       "mouse position": None,
                       }
        # update event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.events["game quit"] = True
            # player click action
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                self.events["mouse position"] = [x, y]

    def update_view(self):
        # render background
        self.view.draw_bg()
        self.view.draw_menu(self.model.menu)
        self.view.draw_ally(self.model.allies)
        self.view.draw_enemies(self.model.enemies)
        self.view.draw_mana_bar(self.model.mana)

    def update_game_over_view(self):
        """draw the ending page when game is over"""
        self.view.draw_game_over(self.model.result)

    def update_game_over_model(self):
        """update used when game over"""
        self.model.result.update(self.events)

    @property
    def quit_game(self):
        return self.events["game quit"]

    @property
    def game_over(self):
        return self.model.game_over

    @property
    def unlock_next_level(self):
        return self.model.unlock_next_level

    @property
    def jump_page_data(self):
        return self.model.result.response, self.model.result.jump_page
