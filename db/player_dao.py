from db.abstract_dao import AbstractDAO


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
