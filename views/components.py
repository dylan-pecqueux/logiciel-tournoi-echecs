from rich.console import Console
from rich.table import Table


class Components:
    def __init__(self):
        self.console = Console()

    def players_table(self, players):
        table = Table(show_header=True, header_style="bold red")
        table.add_column("Rank", style="dim")
        table.add_column("Name", justify="right")
        table.add_column("Gender", justify="right")
        table.add_column("Date of birth", justify="right")
        for player in players:
            table.add_row(
                f"{player.classment}",
                f"[magenta]{player.first_name} {player.last_name}[/magenta]",
                player.sex,
                player.date_of_birth,
            )
        self.console.print(table)
