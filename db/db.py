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

    def update_tournament(self, tournament, id):
        self.tournaments_table.update(tournament, doc_ids=[id])

    def all_players(self):
        serialized_players = self.players_table.all()
        return serialized_players

    def all_tournaments(self):
        serialized_tournaments = self.tournaments_table.all()
        return serialized_tournaments

    def add_player(self, player):
        self.players.append(player)

    def add_tournament(self, tournament):
        self.tournaments.append(tournament)

    def lenght_players_table(self):
        return len(self.players_table)

    def lenght_tournaments_table(self):
        return len(self.tournaments_table)
