from abc import ABC
from db.players_db import DB


class AbstractDAO(ABC):
    def __init__(self):
        self.db = DB()
