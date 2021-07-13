from rich.console import Console
from rich.table import Table


class Components:
    def __init__(self):
        self.console = Console()

    def players_table(self, players, players_list=False):
        table = Table(show_header=True, header_style="bold red")
        table.add_column("Classement", style="dim")
        table.add_column("Nom", justify="right")
        table.add_column("Genre", justify="right")
        table.add_column("Date de naissance", justify="right")
        for player in players:
            if players_list:
                player = player[0]
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

    def matches_table(self, matches):
        table = Table(show_header=True, header_style="bold red")
        table.add_column("Numero", style="dim")
        table.add_column("Match", justify="right")
        for index, match in enumerate(matches):
            (match,) = match
            table.add_row(
                f"{index + 1}",
                f"[bold red]{match.first_player[0].first_name} {match.first_player[0].last_name}[/bold red] contre [bold red]{match.second_player[0].first_name} {match.second_player[0].last_name}[/bold red]",
            )
        self.console.print(table)

    def tournaments_table(self, tournaments, all_tournaments):
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Numero", style="dim")
        table.add_column("Nom")
        table.add_column("Lieu", justify="right")
        table.add_column("Date", justify="right")
        for tournament in tournaments:
            index = all_tournaments.index(tournament)
            table.add_row(
                f"{index + 1}",
                tournament.name,
                tournament.location,
                f"Du {tournament.start_date.date()} au {tournament.end_date.date()}",
            )
        self.console.print(table)
