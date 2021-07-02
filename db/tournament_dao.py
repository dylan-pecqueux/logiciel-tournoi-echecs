from db.abstract_dao import AbstractDAO
from db.serialize_tournament import SerializeTournament
from db.deserialize_tournament import DeserializeTournament


class TournamentDAO(AbstractDAO):
    def __init__(self, all_players):
        super().__init__()
        self.all_players = all_players
        self.serialize_tournament = SerializeTournament()
        self.deserialize_tournament = DeserializeTournament(self.all_players)

    def save(self, tournament):
        serialized_tournament = self.serialize_tournament.serialized_tournament(
            tournament
        )
        self.db.save_tournament(serialized_tournament)
        self.add_tournament(tournament)

    def all_tournaments(self):
        return self.db.all_tournaments()

    def add_tournament(self, tournament):
        self.db.add_tournament(tournament)

    def get_tournaments(self):
        return self.db.tournaments

    def update_tournament(self, tournament):
        serialized_tournament = self.serialize_tournament.serialized_tournament(
            tournament
        )
        self.db.update_tournament(serialized_tournament, tournament.id)

    def give_id(self):
        lenght_tournaments_table = self.db.lenght_tournaments_table()
        next_id = lenght_tournaments_table + 1
        return next_id

    def load_tournaments(self):
        tournaments = self.all_tournaments()
        loaded_tournament = self.deserialize_tournament.deserialized_tournaments(
            tournaments
        )
        self.db.tournaments = loaded_tournament
