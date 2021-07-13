from rich.console import Console
from rich.table import Table

console = Console()


class RoundView:
    def display_all_matchs(self, round):
        print("\033c")
        console.print(
            f"Round {round.round_number}: \n",
            style="bold red",
        )
        console.print(
            f"\nVoici les prochains matchs : \n",
            style="bold red",
        )
        table = Table(show_header=True, header_style="bold red")
        table.add_column("Numero", style="dim")
        table.add_column("Match", justify="right")
        for index, match in enumerate(round.all_matchs):
            (match,) = match
            table.add_row(
                f"{index + 1}",
                f"{match.first_player[0].first_name} {match.first_player[0].last_name} contre {match.second_player[0].first_name} {match.second_player[0].last_name}",
            )
        console.print(table)
        console.print(
            f'\nEntrez "y" quand le round est terminer, pour passer à la notation des scores : ',
            style="bold red",
        )
        end_of_round = input("=> ")
        return end_of_round

    def input_score(self, match):
        print("\033c")
        console.print(f"Entrez les résultats du match {match}\n", style="bold red")
        console.print(f"1 - {match.first_player[0].first_name}", style="bold magenta")
        console.print(f"2 - {match.second_player[0].first_name}", style="bold magenta")
        console.print(
            '\nEntrez le numéro du joueur gagnant ou "eg" en cas de match nul',
            style="bold red",
        )
        winner = input("=> ")
        return winner

    def display_classment_players(self, players):
        print("\033c")
        console.print("Voici le classement provisoire \n", style="bold red")
        table = Table(show_header=True, header_style="bold red")
        table.add_column("Score", style="dim")
        table.add_column("Nom", justify="right")
        table.add_column("Genre", justify="right")
        table.add_column("Classement", justify="right")
        for player in players:
            table.add_row(
                f"{player[1]}",
                f"[magenta]{player[0].first_name} {player[0].last_name}[/magenta]",
                player[0].sex,
                f"{player[0].classment}",
            )
        console.print(table)
        console.print("\nAppuyez sur entrée pour continuer", style="bold red")
        input("=> ")
