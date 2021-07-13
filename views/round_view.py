from rich.console import Console
from rich.table import Table
from views.components import Components


class RoundView(Components):
    def __init__(self):
        super().__init__()
        self.console = Console()

    def display_all_matchs(self, round):
        print("\033c")
        self.console.print(
            f"Round {round.round_number}: \n",
            style="bold red",
        )
        self.console.print(
            f"\nVoici les prochains matchs : \n",
            style="bold red",
        )
        self.matches_table(round.all_matchs)
        self.console.print(
            f'\nEntrez "y" quand le round est terminer, pour passer à la notation des scores : ',
            style="bold red",
        )
        end_of_round = input("=> ")
        return end_of_round

    def input_score(self, match):
        print("\033c")
        self.console.print(f"Entrez les résultats du match {match}\n", style="bold red")
        self.console.print(
            f"1 - {match.first_player[0].first_name}", style="bold magenta"
        )
        self.console.print(
            f"2 - {match.second_player[0].first_name}", style="bold magenta"
        )
        self.console.print(
            '\nEntrez le numéro du joueur gagnant ou "eg" en cas de match nul',
            style="bold red",
        )
        winner = input("=> ")
        return winner

    def display_classment_players(self, players):
        print("\033c")
        self.console.print("Voici le classement provisoire \n", style="bold red")
        self.classment_table(players)
        self.console.print("\nAppuyez sur entrée pour continuer", style="bold red")
        input("=> ")
