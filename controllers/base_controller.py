from controllers.player_controller import Player_controller


class Controller:

    def __init__(self, view):
        self.view = view

    def menu_choice(self):
        choice = self.view.prompt_for_choice()
        if choice == "1":
            player = Player_controller()
            player.add_player()
        else:
            return

    def run(self):
        self.menu_choice()
