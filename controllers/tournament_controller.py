from models.tournament import Tournament
from models.round import Round
from views.tournament_view import TournamentView
from views.tournaments_view import TournamentsView
from controllers.round_controller import RoundController


class TournamentController:
    def __init__(self, players, tournaments):
        self.tournament_view = TournamentView(players.all_players)
        self.tournaments_view = TournamentsView()
        self.all_tournaments = tournaments.all_tournaments

    def add_tournament(self, tournaments):
        info_tounament = self.tournament_view.prompt_info_tournament()
        new_tournament = Tournament(
            info_tounament[0],
            info_tounament[1],
            info_tounament[2],
            info_tounament[3],
            info_tounament[4],
            info_tounament[5],
            info_tounament[6],
            info_tounament[7],
        )
        new_tournament.sort_players_by_classment()
        tournaments.add_tournament(new_tournament)
        self.tournament_view.display_tournament(new_tournament)

    def view_all_tournaments(self, tournaments):
        tournament_to_view = self.tournaments_view.display_all_tournaments(
            tournaments.all_tournaments
        )
        if tournament_to_view == "10":
            return
        else:
            start_tournament_or_not = self.tournament_view.display_tournament_info(
                self.all_tournaments[int(tournament_to_view)]
            )
            if start_tournament_or_not == "1":
                self.start_tournament(self.all_tournaments[int(tournament_to_view)])

    def start_tournament(self, tournament):
        starter_round = RoundController()
        tournament.add_round(starter_round.round)
        starter_round.first_pair_generation(tournament.players_list)
        starter_round.input_score(tournament.players_list)
        for i in range(3):
            print("ça passe ici")
            self.new_round(tournament)

    def new_round(self, tournament):
        start_new_round = RoundController()
        tournament.add_round(start_new_round.round)
        start_new_round.pair_generation(tournament.players_list)
        start_new_round.input_score(tournament.players_list)
