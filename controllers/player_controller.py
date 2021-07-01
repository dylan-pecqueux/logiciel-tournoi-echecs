from models.player import Player
from views.players_view import PlayersView
from db.player_dao import PlayerDAO


class PlayerController:
    def __init__(self):
        """Has a view and a list of players"""
        self.view = PlayersView()
        self.player_dao = PlayerDAO()

    def add_player(self, all_players):
        """Had a player"""
        info_player = self.view.prompt_for_player()
        new_player = Player(
            info_player[0],
            info_player[1],
            info_player[2],
            info_player[3],
            int(info_player[4]),
        )
        self.player_dao.save(new_player)
        self.view.display_player(new_player)
        all_players.add_player_to_list(new_player)

    def add_another_player(self):
        return self.view.prompt_add_another_player() == "y"

    def view_all_players(self, players):
        self.view.display_all_players(players.all_players)
