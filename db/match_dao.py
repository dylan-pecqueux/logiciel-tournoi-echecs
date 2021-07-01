from db.abstract_dao import AbstractDAO


class MatchDAO(AbstractDAO):
    def save(self, match):
        self.db.save(match)
