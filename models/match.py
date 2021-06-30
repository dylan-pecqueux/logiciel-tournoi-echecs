class Match:
    def __init__(self, player_1, player_2):
        self.first_player = [player_1, 0]
        self.second_player = [player_2, 0]

    def __str__(self):
        return f"{self.first_player[0].first_name} {self.first_player[0].last_name} contre {self.second_player[0].first_name} {self.second_player[0].last_name}"
