from models.player import Player
from views.players_view import PlayersView


class PlayerController:

    def __init__(self):
        """Has a view and a list of players"""
        self.view = PlayersView()
        self.players = []

    def add_player(self):
        """Had a player"""
        info_player = self.view.prompt_for_player()
        new_player = Player(info_player[0], info_player[1],
                            info_player[2], info_player[3],
                            info_player[4])
        self.view.display_player(new_player)
        self.players.append(new_player)

    def add_another_player(self):
        return self.view.prompt_add_another_player() == "y"

    def view_all_players(self):
        self.view.display_all_players(self.players)
