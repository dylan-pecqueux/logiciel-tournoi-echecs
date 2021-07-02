from models.tournament import Tournament
from models.round import Round
from views.tournament_view import TournamentView
from views.tournaments_view import TournamentsView
from controllers.round_controller import RoundController


class TournamentController:
    def __init__(self, players, tournament_dao):
        self.tournament_view = TournamentView(players)
        self.tournaments_view = TournamentsView()
        self.tournament_dao = tournament_dao

    def add_tournament(self):
        info_tournament = self.tournament_view.prompt_info_tournament()
        new_tournament = Tournament(
            info_tournament[0],
            info_tournament[1],
            info_tournament[2],
            info_tournament[3],
            info_tournament[4],
            info_tournament[5],
            info_tournament[6],
            info_tournament[7],
            self.tournament_dao.give_id(),
        )
        self.tournament_dao.save(new_tournament)
        new_tournament.sort_players_by_classment()
        self.tournament_view.display_tournament(new_tournament)

    def view_all_tournaments(self):
        tournament_to_view = self.tournaments_view.display_all_tournaments(
            self.tournament_dao.get_tournaments()
        )
        if tournament_to_view == "10":
            return
        else:
            start_tournament_or_not = self.tournament_view.display_tournament_info(
                self.tournament_dao.get_tournaments()[int(tournament_to_view)]
            )
            if start_tournament_or_not == "1":
                self.start_tournament(
                    self.tournament_dao.get_tournaments()[int(tournament_to_view)]
                )

    def start_tournament(self, tournament):
        """start tournament and run round 4 time
        i == number of actual round
        """
        starting_round = len(tournament.rounds) + 1
        for i in range(starting_round, 5):
            start_new_round = RoundController(i)
            tournament.add_round(start_new_round.round)
            start_new_round.run_round(tournament)
            self.tournament_dao.update_tournament(tournament)
        self.tournament_end(tournament.players_list)

    def tournament_end(self, classment):
        self.tournament_view.display_tournament_end(classment)
