from rich.console import Console
from rich.table import Table

console = Console()


class TournamentView:
    def __init__(self, all_players):
        self.list_of_players = all_players

    def display_tournament_info(self, tournament):
        print("\033c")
        console.print(
            f"[bold red] {tournament.name}[/bold red]\n\n [blue]À {tournament.location}, du {tournament.start_date} au {tournament.end_date}\n {tournament.number_of_turns} tours et {tournament.time_control} en controle du temps.\n\n Commentaire :\n[/blue] {tournament.description}"
        )
        if len(tournament.rounds) >= 4:
            console.print("\nTournoi terminé", style="bold red")
            console.print(
                "\n1 - Voir les rounds du tournoi"
                "\n2 - Voir les joueurs du tournoi"
                "\n0 - Revenir au menu",
                style="bold magenta",
            )
        else:
            console.print("\nTournoi non commencé", style="bold red")
            console.print(
                "\n1 - Commencer le tournoi"
                "\n2 - Voir les joueurs du tournoi"
                "\n0 - Revenir au menu",
                style="bold magenta",
            )
        console.print("\nQue voulez-vous faire ? : ", style="bold red")
        user_choice = input("=> ")
        return user_choice

    def display_all_players(self, players, order):
        print("\033c")
        console.print(
            f"Liste de tous les joueurs du tournoi par {order}: \n", style="bold red"
        )
        table = Table(show_header=True, header_style="bold red")
        table.add_column("Rank", style="dim")
        table.add_column("Nom", justify="right")
        table.add_column("Genre", justify="right")
        table.add_column("Date de naissance", justify="right")
        for player in players:
            player = player[0]
            table.add_row(
                f"{player.classment}",
                f"[magenta]{player.first_name} {player.last_name}[/magenta]",
                player.sex,
                player.date_of_birth,
            )
        console.print(table)
        console.print(
            "\n1 - Joueurs par classement (défaut) \n"
            "2 - Joueurs par ordre alphabétique \n"
            "0 - Revenir au tournoi \n",
            style="bold magenta",
        )
        console.print("Que voulez-vous faire ?", style="bold red")
        user_choice = input("=> ")
        return user_choice

    def display_info_round(self, round):
        print("\033c")
        console.print(
            f"Liste de tous les match du round {round.round_number}: \n",
            style="bold red",
        )
        table = Table(show_header=True, header_style="bold red")
        table.add_column("Match", style="dim")
        table.add_column("Joueurs", justify="right")
        table.add_column("Vainqueur", justify="right")
        for index, match in enumerate(round.all_matchs):
            if match.first_player[1] == 1:
                winner = f"{match.first_player[0].first_name} {match.first_player[0].last_name}"
            elif match.first_player[1] == 0.5:
                winner = "égalité"
            else:
                winner = f"{match.second_player[0].first_name} {match.second_player[0].last_name}"
            table.add_row(
                f"{index + 1}",
                f"{match.first_player[0].first_name} {match.first_player[0].last_name} contre {match.second_player[0].first_name} {match.second_player[0].last_name}",
                winner,
            )
        console.print(table)
        console.print(
            "\n0 - Revenir au tournoi \n",
            style="bold magenta",
        )
        console.print("Que voulez-vous faire ?", style="bold red")
        user_choice = input("=> ")
        return user_choice

    def display_tournament_end(self, classment):
        print("\033c")
        console.print(
            "Tous les rounds ont étaient joués, le tournoi est terminé",
            style="bold red",
        )
        console.print("\nVoici le classement final : \n", style="bold magenta")
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
        console.print(table)
        console.print("\nAppuyez sur entrée pour continuer", style="bold red")
        input("=> ")

    def display_all_rounds(self, tournament):
        print("\033c")
        console.print(
            f"Liste de tous les rounds du tournoi {tournament.name}: \n",
            style="bold red",
        )
        table = Table(show_header=True, header_style="bold red")
        table.add_column("Nom", style="dim")
        table.add_column("Début", justify="right")
        table.add_column("Fin", justify="right")
        for round in tournament.rounds:
            table.add_row(
                f"Round {round.round_number}",
                f"{round.start_date}",
                f"{round.end_date}",
            )
        console.print(table)
        console.print(
            "\n0 - Revenir au tournoi \n",
            style="bold magenta",
        )
        console.print("Que voulez-vous faire ?", style="bold red")
        user_choice = input("=> ")
        return user_choice
