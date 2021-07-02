from models.match import Match


class Round:
    def __init__(self, round_number=1, all_matchs=[]):
        self.all_matchs = all_matchs
        self.round_number = round_number

    def new_match(self, player_1, player_2, tournament):
        new_match = Match(player_1, player_2, tournament)
        self.all_matchs.append(new_match)
