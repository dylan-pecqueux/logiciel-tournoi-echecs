class Match:
    def __init__(self, player_1, player_2, score=None):
        self.first_player = [player_1, score]
        self.second_player = [player_2, score]

    def __str__(self):
        return f"{self.first_player[0].first_name} {self.first_player[0].last_name} contre {self.second_player[0].first_name} {self.second_player[0].last_name}"
