from models.match import Match


class Round:
    def __init__(self, round_number=1):
        self.all_matchs = []
        self.round_number = round_number

    def new_match(self, player_1, player_2):
        new_match = Match(player_1, player_2)
        self.all_matchs.append(new_match)
