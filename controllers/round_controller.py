from models.round import Round
from views.round_view import RoundView


class RoundController:
    def __init__(self):
        self.round = Round()
        self.round_view = RoundView()

    def first_pair_generation(self, players):
        self.round.new_match(players[0][0], players[1][0])
        self.view_round()

    def pair_generation(self, players):
        self.round.new_match(players[0][0], players[1][0])
        self.view_round()

    def view_round(self):
        end_of_round = None
        while end_of_round != "y":
            end_of_round = self.round_view.display_all_matchs(self.round.all_matchs)

    def find_player(self, winner_player, all_players, score):
        """Add new score in tournament players list"""
        for player in all_players:
            if winner_player[0] == player[0]:
                player[1] += score
                print("ça marche bien")
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

    def run_round():
        pass
