import datetime
from rich.console import Console
from rich.table import Table

console = Console()


class TournamentsView:
    def display_all_tournaments(self, tournaments):
        print("\033c")
        now = datetime.datetime.now()
        past_tournaments = []
        future_tournaments = []
        for tournament in tournaments:
            if tournament.end_date > now:
                future_tournaments.append(tournament)
            else:
                past_tournaments.append(tournament)
        console.print("Tournois passés :", style="bold red")
        if past_tournaments:
            self.create_table(past_tournaments)
        console.print("\nTournois futurs :", style="bold red")
        if future_tournaments:
            self.create_table(future_tournaments)

        console.print("\n0 - Revenir au menu\n", style="bold magenta")
        console.print(
            "Tapez le numéro du tournoi que vous voulez voir : ", style="bold red"
        )
        user_choice = input("=> ")
        return int(user_choice) - 1

    def create_table(self, tournaments):
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Numero", style="dim")
        table.add_column("Nom")
        table.add_column("Lieu", justify="right")
        table.add_column("Date", justify="right")
        for tournament in tournaments:
            index = tournaments.index(tournament)
            table.add_row(
                f"{index + 1}",
                tournament.name,
                tournament.location,
                f"Du {tournament.start_date} au {tournament.end_date}",
            )
        console.print(table)
