from db.abstract_dao import AbstractDAO
from models.player import Player


class PlayerDAO(AbstractDAO):
    def save(self, player):
        serialized_player = self.serialized_player(player)
        self.db.save(serialized_player)

    def serialized_player(self, player):
        serialized_player = {
            "last_name": player.last_name,
            "first_name": player.first_name,
            "date_of_birth": player.date_of_birth,
            "sex": player.sex,
            "classment": player.classment,
        }
        return serialized_player

    def get_players(self):
        return self.db.players

    def all_players(self):
        return self.db.all_players()

    def add_player(self, player):
        self.db.add_player(player)

    def deserialized_players(self):
        players = self.all_players()
        for player in players:
            last_name = player["last_name"]
            first_name = player["first_name"]
            date_of_birth = player["date_of_birth"]
            sex = player["sex"]
            classment = player["classment"]
            load_player = Player(last_name, first_name, date_of_birth, sex, classment)
            self.add_player(load_player)
