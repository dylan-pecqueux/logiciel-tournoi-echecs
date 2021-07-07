import datetime
from rich.console import Console
from rich.table import Table

console = Console()


class TournamentsView:
    def display_all_tournaments(self, tournaments):
        print("\033c")
        now = datetime.datetime.now().date()
        past_tournaments = []
        future_tournaments = []
        for tournament in tournaments:
            end_date = tournament.end_date.split("/")
            date = datetime.date(int(end_date[2]), int(end_date[1]), int(end_date[0]))
            if date > now:
                future_tournaments.append(tournament)
            else:
                past_tournaments.append(tournament)
        console.print("Tournois passés :", style="bold red")
        if past_tournaments:
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("Numero", style="dim")
            table.add_column("Nom")
            table.add_column("Lieu", justify="right")
            table.add_column("Date", justify="right")
            for tournament in past_tournaments:
                index = tournaments.index(tournament)
                table.add_row(
                    f"{index + 1}",
                    tournament.name,
                    tournament.location,
                    f"Du {tournament.start_date} au {tournament.end_date}",
                )
            console.print(table)
        console.print("\nTournois futurs :", style="bold red")
        if future_tournaments:
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("Numero", style="dim")
            table.add_column("Nom")
            table.add_column("Lieu", justify="right")
            table.add_column("Date", justify="right")
            for tournament in future_tournaments:
                index = tournaments.index(tournament)
                table.add_row(
                    f"{index + 1}",
                    tournament.name,
                    tournament.location,
                    f"Du {tournament.start_date} au {tournament.end_date}",
                )
            console.print(table)

        console.print("\n0 - Revenir au menu\n", style="bold magenta")
        console.print(
            "Tapez le numéro du tournoi que vous voulez voir : ", style="bold red"
        )
        user_choice = input("=> ")
        return int(user_choice) - 1
