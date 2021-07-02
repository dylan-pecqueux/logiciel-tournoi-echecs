from tinydb import TinyDB


class DB:
    def __init__(self):
        self.players = []
        self.tournaments = []
        self.db = TinyDB("db.json")
        self.players_table = self.db.table("players")
        self.tournaments_table = self.db.table("tournaments")

    def save_player(self, player):
        self.players_table.insert(player)

    def save_tournament(self, tournament):
        self.tournaments_table.insert(tournament)

    def all_players(self):
        serialized_players = self.players_table.all()
        return serialized_players

    def add_player(self, player):
        self.players.append(player)

    def add_tournament(self, tournament):
        self.tournaments.append(tournament)
