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
        index_tournament_to_view = self.tournaments_view.display_all_tournaments(
            self.tournament_dao.get_tournaments()
        )
        if index_tournament_to_view == "0":
            return
        else:
            tournament = self.tournament_dao.get_tournaments()[index_tournament_to_view]
            self.view_tournament(tournament)

    def view_tournament(self, tournament):
        user_choice = self.tournament_view.display_tournament_info(tournament)
        if len(tournament.rounds) < 4:
            self.menu_begin_tournament(tournament, user_choice)
        else:
            self.menu_ended_tournament(tournament, user_choice)

    def menu_begin_tournament(self, tournament, user_choice):
        if user_choice == "1":
            self.start_tournament(tournament)
        elif user_choice == "2":
            self.view_players_from_tournament(tournament)
            self.view_tournament(tournament)

    def menu_ended_tournament(self, tournament, user_choice):
        if user_choice == "1":
            self.view_round_of_tournament(tournament)
            self.view_tournament(tournament)
        elif user_choice == "2":
            self.view_players_from_tournament(tournament)
            self.view_tournament(tournament)

    def view_round_of_tournament(self, tournament):
        user_choice = self.tournament_view.display_all_rounds(tournament)
        try:
            selected_round = tournament.rounds[int(user_choice) - 1]
        except:
            selected_round = None
        if selected_round:
            self.view_info_round(selected_round)

    def view_info_round(self, round):
        self.tournament_view.display_info_round(round)

    def view_players_from_tournament(self, tournament, user_choice="1"):
        if user_choice == "1":
            players_by_classment = self.sort_players_by_classment(tournament)
            user_choice = self.tournament_view.display_all_players(
                players_by_classment, "classement"
            )
            self.view_players_from_tournament(tournament, user_choice)
        elif user_choice == "2":
            players_by_alphabetics = self.sort_players_by_alphabetics(tournament)
            user_choice = self.tournament_view.display_all_players(
                players_by_alphabetics, "ordre alphabétique"
            )
            self.view_players_from_tournament(tournament, user_choice)

    def sort_players_by_classment(self, tournament):
        players = tournament.players_list
        players_by_classment = sorted(players, key=lambda player: player[0].classment)
        return players_by_classment

    def sort_players_by_alphabetics(self, tournament):
        players = tournament.players_list
        players_by_alphabetics = sorted(players, key=lambda player: player[0].last_name)
        return players_by_alphabetics

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
