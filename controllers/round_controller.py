from models.round import Round
from views.round_view import RoundView


class RoundController:
    def __init__(self, round_number):
        self.round = Round()
        self.round_view = RoundView()
        self.round_number = round_number

    def first_pair_generation(self, players):
        """Suiss algo : Split in two list players list by middle and associate the player with the same index in the other list"""
        first_list = players[: len(players) // 2]
        second_list = players[len(players) // 2 :]

        for index, player in enumerate(first_list):
            self.round.new_match(player[0], second_list[index][0])

    def pair_generation(self, tournament):
        for round in tournament.rounds:
            if (
                self.round.new_match(
                    tournament.players_list[0][0], tournament.players_list[1][0]
                )
                in round.all_matchs
            ):
                pass
        self.round.new_match(
            tournament.players_list[0][0], tournament.players_list[1][0]
        )

    def view_round(self):
        end_of_round = None
        while end_of_round != "y":
            end_of_round = self.round_view.display_all_matchs(self.round.all_matchs)

    def find_player(self, winner_player, all_players, score):
        """Add new score in tournament players list"""
        for player in all_players:
            if winner_player[0] == player[0]:
                player[1] += score
                break

    def input_score(self, all_players):
        for match in self.round.all_matchs:
            self.add_score(match, all_players)

    def add_score(self, match, all_players):
        winner = self.round_view.input_score(match)
        if winner == "1":
            match.first_player[1] = 1
            self.find_player(match.first_player, all_players, 1)
        elif winner == "2":
            match.second_player[1] = 1
            self.find_player(match.second_player, all_players, 1)
        elif winner == "eg":
            match.first_player[1] = 0.5
            match.second_player[1] = 0.5
            self.find_player(match.first_player, all_players, 0.5)
            self.find_player(match.second_player, all_players, 0.5)
        else:
            self.add_score(match, all_players)

    def sort_players(self, tournament):
        tournament.sort_players_by_score()
        self.display_classment_players(tournament.players_list)

    def display_classment_players(self, players):
        self.round_view.display_classment_players(players)

    def run_round(self, tournament):
        if self.round_number == 1:
            self.first_pair_generation(tournament.players_list)
        else:
            self.pair_generation(tournament)
        self.view_round()
        self.input_score(tournament.players_list)
        self.sort_players(tournament)
