from rich.console import Console
from rich.table import Table


class Components:
    def __init__(self):
        self.console = Console()

    def players_table(self, players):
        table = Table(show_header=True, header_style="bold red")
        table.add_column("Classement", style="dim")
        table.add_column("Nom", justify="right")
        table.add_column("Genre", justify="right")
        table.add_column("Date de naissance", justify="right")
        for player in players:
            table.add_row(
                f"{player.classment}",
                f"[magenta]{player.first_name} {player.last_name}[/magenta]",
                player.sex,
                player.date_of_birth,
            )
        self.console.print(table)

    def classment_table(self, classment):
        table = Table(show_header=True, header_style="bold red")
        table.add_column("Score", style="dim")
        table.add_column("Nom", justify="right")
        table.add_column("Genre", justify="right")
        table.add_column("Classement", justify="right")
        for player in classment:
            table.add_row(
                f"{player[1]}",
                f"[magenta]{player[0].first_name} {player[0].last_name}[/magenta]",
                player[0].sex,
                f"{player[0].classment}",
            )
        self.console.print(table)

    def rounds_table(self, rounds):
        table = Table(show_header=True, header_style="bold red")
        table.add_column("Nom", style="dim")
        table.add_column("Début", justify="right")
        table.add_column("Fin", justify="right")
        for round in rounds:
            table.add_row(
                f"Round {round.round_number}",
                f"{round.start_date}",
                f"{round.end_date}",
            )
        self.console.print(table)

    def info_round_table(self, matches):
        table = Table(show_header=True, header_style="bold red")
        table.add_column("Match", style="dim")
        table.add_column("Joueurs", justify="right")
        table.add_column("Vainqueur", justify="right")
        for index, match in enumerate(matches):
            (match,) = match
            if match.first_player[1] == 1:
                winner = f"{match.first_player[0].first_name} {match.first_player[0].last_name}"
            elif match.first_player[1] == 0.5:
                winner = "égalité"
            else:
                winner = f"{match.second_player[0].first_name} {match.second_player[0].last_name}"
            table.add_row(
                f"{index + 1}",
                f"[bold red]{match.first_player[0].first_name} {match.first_player[0].last_name}[/bold red] contre [bold red]{match.second_player[0].first_name} {match.second_player[0].last_name}[/bold red]",
                winner,
            )
        self.console.print(table)
