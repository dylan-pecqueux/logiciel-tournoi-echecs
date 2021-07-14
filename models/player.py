class Player:
    def __init__(self, last_name, first_name, date_of_birth, sex, classment, id):
        """Has last name, first name, date of birth (dd/mm/aaaa), sex (m or f)
        and a positive number for classment
        """
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.classment = classment
        self.id = id
        self.matches = []

    def play_match(self, match):
        self.matches.append(match)

    def get_matches_by_tournament(self, tournament):
        return [match for match in self.matches if match.tournament == tournament]

    def get_opponents(self, tournament):
        result = []
        for match in self.get_matches_by_tournament(tournament):
            if match.first_player[0] != self:
                result.append(match.first_player[0])
            else:
                result.append(match.second_player[0])
        return result

    def __str__(self):
        """Used for print player in view"""
        return f" {self.first_name} {self.last_name}\n {self.sex}\n né le : {self.date_of_birth}\n \
        classement : {self.classment}"
