from db.abstract_dao import AbstractDAO


class TournamentDAO(AbstractDAO):
    def save(self, tournament):
        serialized_tournament = self.serialized_tournament(tournament)
        self.db.save_tournament(serialized_tournament)

    def serialized_tournament(self, tournament):
        serialized_tournament = {
            "name": tournament.name,
            "location": tournament.location,
            "start_date": tournament.start_date,
            "end_date": tournament.end_date,
            "number_of_turns": tournament.number_of_turns,
            "players_list": tournament.players_list,
            "time_control": tournament.time_control,
            "description": tournament.description,
        }
        return serialized_tournament
