from models.round import Round
from views.round_view import RoundView


class RoundController:
    def __init__(self):
        self.round = Round()
        self.round_view = RoundView()

    def first_pair_generation(self, players):
        self.round.new_match(players[0], players[1])
        self.view_round()

    def other_pair_generation(self, players):
        pass

    def view_round(self):
        end_of_round = None
        while end_of_round != "y":
            end_of_round = self.round_view.display_all_matchs(self.round.all_matchs)
        self.add_score()

    def add_score(self):
        self.round_view.input_score(self.round.all_matchs)
