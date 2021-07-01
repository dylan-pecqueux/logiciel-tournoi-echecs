from abc import ABC
from db.players_db import PlayersDB


class AbstractDAO(ABC):
    def __init__(self):
        self.db = PlayersDB()
