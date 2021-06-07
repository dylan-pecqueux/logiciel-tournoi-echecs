from models.player import Player
from views.players import Players


class Player_controller:

    def __init__(self):
        self.view = Players()
        self.players = []

    def add_player(self):
        info_player = self.view.prompt_for_player()
        player = Player(info_player[0], info_player[1],
                        info_player[2], info_player[3],
                        info_player[4])
        self.view.display_player(player)
        self.players.append(player)
