from tinydb import TinyDB


class PlayersDB:
    def __init__(self):
        self.db = TinyDB("db.json")
        self.players_table = self.db.table("players")

    def save(self, player):
        self.players_table.insert(player)
