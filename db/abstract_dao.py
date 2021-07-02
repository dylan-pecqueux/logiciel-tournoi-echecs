from abc import ABC
from db.db import DB


class AbstractDAO(ABC):
    def __init__(self):
        self.db = DB()
