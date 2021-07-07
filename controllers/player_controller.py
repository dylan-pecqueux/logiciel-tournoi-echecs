from models.player import Player
from views.players_view import PlayersView


class PlayerController:
    def __init__(self, player_dao):
        """Has a view and a list of players"""
        self.view = PlayersView()
        self.player_dao = player_dao

    def add_player(self):
        """Had a player"""
        info_player = self.view.prompt_for_player()
        new_player = Player(
            info_player[0],
            info_player[1],
            info_player[2],
            info_player[3],
            int(info_player[4]),
            self.player_dao.give_id(),
        )
        self.player_dao.save(new_player)
        self.view.display_player(new_player)

    def add_another_player(self):
        return self.view.prompt_add_another_player() == "y"

    def view_all_players(self):
        players_by_classment = self.sort_players_by_classment()
        self.view.display_all_players(players_by_classment)

    def sort_players_by_classment(self):
        players = self.player_dao.get_players()
        players_by_classment = sorted(players, key=lambda player: player.classment)
        return players_by_classment
