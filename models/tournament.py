class Tournament:
    def __init__(
        self,
        name,
        location,
        start_date,
        end_date,
        number_of_turns,
        players_list,
        time_control,
        description,
    ):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_turns = number_of_turns
        self.players_list = players_list
        self.time_control = time_control
        self.description = description
        self.rounds = []

    def sort_players_by_classment(self):
        self.players_list = sorted(
            self.players_list, key=lambda player: player[0].classment
        )

    def add_round(self, round):
        self.rounds.append(round)

    def name_and_date(self):
        return f"{self.name}, début le {self.start_date}"

    def __str__(self):
        """Used for print player in view"""
        return f" {self.name}\n lieu : {self.location}\n du {self.start_date} au {self.end_date}\n nombre de tours {self.number_of_turns}, controle du temps : {self.time_control}\n {self.description}\n Joueurs du tournoi : \n {self.players_list[0]}\n {self.players_list[1]}"
