from views.tournament_view import TournamentView
from models.tournament import Tournament


class TournamentController:

    def __init__(self, players):
        self.view = TournamentView(players.all_players)

    def add_tournament(self):
        info_tounament = self.view.prompt_info_tournament()
        new_tournament = Tournament(info_tounament[0], info_tounament[1], info_tounament[2], info_tounament[3],
                                    info_tounament[4], info_tounament[5], info_tounament[6], info_tounament[7])
        self.view.display_tournament(new_tournament)
