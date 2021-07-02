from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from models.tournaments import Tournaments
from db.player_dao import PlayerDAO
from db.tournament_dao import TournamentDAO


class BaseController:
    """Main controller"""

    def __init__(self, view):
        """Has a view"""
        self.player_dao = PlayerDAO()
        self.tournament_dao = TournamentDAO()
        self.load_players_in_db()
        self.view = view
        self.player_controller = PlayerController(self.player_dao)
        self.tournaments = Tournaments()
        self.tournament_controller = TournamentController(
            self.player_dao.get_players(), self.tournaments, self.tournament_dao
        )

    def load_players_in_db(self):
        self.player_dao.deserialized_players()

    def menu_choice(self):
        """Navigate in to the programm"""
        user_choice = self.view.prompt_for_choice()
        if user_choice == "1":
            self.player_controller.add_player()
            while self.player_controller.add_another_player():
                self.player_controller.add_player()
            self.menu_choice()
        if user_choice == "2":
            self.player_controller.view_all_players()
            self.menu_choice()
        if user_choice == "3":
            self.tournament_controller.add_tournament(self.tournaments)
            self.menu_choice()
        if user_choice == "4":
            self.tournament_controller.view_all_tournaments(self.tournaments)
            self.menu_choice()

    def run(self):
        """Run the programm"""
        self.menu_choice()
