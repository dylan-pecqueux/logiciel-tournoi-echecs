from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from models.players import Players


class BaseController:
    """Main controller"""

    def __init__(self, view):
        """Has a view"""
        self.view = view
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController()
        self.players = Players()

    def menu_choice(self):
        """Navigate in to the programm"""
        user_choice = self.view.prompt_for_choice()
        if user_choice == "1":
            self.player_controller.add_player(self.players)
            while self.player_controller.add_another_player():
                self.player_controller.add_player(self.players)
            self.menu_choice()
        if user_choice == "2":
            self.player_controller.view_all_players(self.players)
            self.menu_choice()
        if user_choice == "3":
            self.tournament_controller.add_tournament(self.players)

    def run(self):
        """Run the programm"""
        self.menu_choice()
