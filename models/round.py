from datetime import datetime
from models.match import Match


class Round:
    def __init__(self, round_number, start_date, end_date=None):
        self.all_matchs = []
        self.round_number = round_number
        self.start_date = start_date
        self.end_date = end_date

    def new_match(self, player_1, player_2, tournament):
        new_match = Match(player_1, player_2, tournament)
        self.all_matchs.append((new_match,))

    def add_end_date(self):
        self.end_date = datetime.now()
