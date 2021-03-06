class Match:
    def __init__(
        self, player_1, player_2, tournament, score_player_1=0, score_player_2=0
    ):
        self.first_player = [player_1, score_player_1]
        self.second_player = [player_2, score_player_2]
        self.tournament = tournament
        self.first_player[0].play_match(self)
        self.second_player[0].play_match(self)

    def __str__(self):
        return f"{self.first_player[0].first_name} {self.first_player[0].last_name} contre \
        {self.second_player[0].first_name} {self.second_player[0].last_name}"
