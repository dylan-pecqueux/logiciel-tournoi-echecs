from models.player import Player


class Controller:

    def __init__(self, view):
        self.players = []
        self.view = view

    def add_player(self):
        while len(self.players) < 5:
            name = self.view.prompt_for_player()
            if not name:
                return
            player = Player(name)
            self.players.append(player)

    def run(self):
        self.add_player()
