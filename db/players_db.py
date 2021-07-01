from tinydb import TinyDB


class PlayersDB:
    def __init__(self):
        self.players = []
        self.db = TinyDB("db.json")
        self.players_table = self.db.table("players")

    def save(self, player):
        self.players_table.insert(player)

    def all_players(self):
        serialized_players = self.players_table.all()
        return serialized_players

    def add_player(self, player):
        self.players.append(player)
