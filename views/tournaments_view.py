import datetime
from rich.console import Console
from views.components import Components


class TournamentsView(Components):
    def __init__(self):
        super().__init__()
        self.console = Console()

    def display_all_tournaments(self, tournaments):
        """Display tournaments in 3 different tables :
        - Past
        - Present
        - Future
        """
        print("\033c")
        now = datetime.datetime.now().date()
        past_tournaments = []
        present_tournaments = []
        future_tournaments = []
        for tournament in tournaments:
            if (
                tournament.end_date.date() >= now and tournament.start_date.date() <= now
            ):
                present_tournaments.append(tournament)
            elif tournament.start_date.date() > now:
                future_tournaments.append(tournament)
            else:
                past_tournaments.append(tournament)
        self.console.print("Tournois passés :", style="bold red")
        self.tournaments_table(past_tournaments, tournaments)
        self.console.print("\nTournois du jour :", style="bold red")
        self.tournaments_table(present_tournaments, tournaments)
        self.console.print("\nTournois futurs :", style="bold red")
        self.tournaments_table(future_tournaments, tournaments)

        self.console.print("\n0 - Revenir au menu\n", style="bold magenta")
        self.console.print(
            "Tapez le numéro du tournoi que vous voulez voir : ", style="bold red"
        )
        user_choice = input("=> ")
        if user_choice and user_choice != "0":
            return int(user_choice) - 1
        else:
            return None
