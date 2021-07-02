from db.abstract_dao import AbstractDAO


class TournamentDAO(AbstractDAO):
    def save(self, tournament):
        serialized_tournament = self.serialized_tournament(tournament)
        self.db.save_tournament(serialized_tournament)

    def serialized_tournament(self, tournament):
        pass
