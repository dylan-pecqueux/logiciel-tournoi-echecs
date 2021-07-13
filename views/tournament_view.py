from rich.console import Console
from views.components import Components


class TournamentView(Components):
    def __init__(self, all_players):
        super().__init__()
        self.list_of_players = all_players
        self.console = Console()

    def display_tournament_info(self, tournament):
        print("\033c")
        self.console.print(
            f"[bold red] {tournament.name}[/bold red]\n\n [blue]À {tournament.location}, du {tournament.start_date.date()} au {tournament.end_date.date()}\n {tournament.number_of_turns} tours et {tournament.time_control} en controle du temps.\n\n Commentaire :\n[/blue] {tournament.description}"
        )
        if len(tournament.rounds) >= 4:
            self.console.print("\nTournoi terminé", style="bold red")
            self.console.print(
                "\n1 - Voir les rounds du tournoi"
                "\n2 - Voir les joueurs du tournoi"
                "\n0 - Revenir au menu",
                style="bold magenta",
            )
        else:
            self.console.print("\nTournoi non commencé", style="bold red")
            self.console.print(
                "\n1 - Commencer le tournoi"
                "\n2 - Voir les joueurs du tournoi"
                "\n0 - Revenir au menu",
                style="bold magenta",
            )
        self.console.print("\nQue voulez-vous faire ? : ", style="bold red")
        user_choice = input("=> ")
        return user_choice

    def display_all_players(self, players, order):
        print("\033c")
        self.console.print(
            f"Liste de tous les joueurs du tournoi par {order}: \n", style="bold red"
        )
        self.players_table(players, True)
        self.console.print(
            "\n1 - Joueurs par classement (défaut) \n"
            "2 - Joueurs par ordre alphabétique \n"
            "0 - Revenir au tournoi \n",
            style="bold magenta",
        )
        self.console.print("Que voulez-vous faire ?", style="bold red")
        user_choice = input("=> ")
        return user_choice

    def display_info_round(self, round):
        print("\033c")
        self.console.print(
            f"Liste de tous les match du round {round.round_number}: \n",
            style="bold red",
        )
        self.info_round_table(round.all_matchs)
        self.console.print(
            "\n0 - Revenir au tournoi \n",
            style="bold magenta",
        )
        self.console.print("Que voulez-vous faire ?", style="bold red")
        user_choice = input("=> ")
        return user_choice

    def display_tournament_end(self, classment):
        print("\033c")
        self.console.print(
            "Tous les rounds ont étaient joués, le tournoi est terminé",
            style="bold red",
        )
        self.console.print("\nVoici le classement final : \n", style="bold magenta")
        self.classment_table(classment)
        self.console.print("\nAppuyez sur entrée pour continuer", style="bold red")
        input("=> ")

    def display_all_rounds(self, tournament):
        print("\033c")
        self.console.print(
            f"Liste de tous les rounds du tournoi {tournament.name}: \n",
            style="bold red",
        )
        self.rounds_table(tournament.rounds)
        self.console.print(
            "\nEntrez le numero du round que vous voulez voir"
            "\n0 - Revenir au tournoi \n",
            style="bold magenta",
        )
        self.console.print("Que voulez-vous faire ?", style="bold red")
        user_choice = input("=> ")
        return user_choice
