from rich.console import Console
from rich.table import Table

console = Console()


class TournamentView:
    def __init__(self, all_players):
        self.list_of_players = all_players

    def prompt_info_tournament(self):
        info_tounament = []

        name = input("Entrez le nom du tournoi : ")
        info_tounament.append(name)
        location = input("Entrez le lieu du tournoi : ")
        info_tounament.append(location)
        start_date = input("Entrez la date de début : ")
        info_tounament.append(start_date)
        end_date = input("Entrez la date de fin : ")
        info_tounament.append(end_date)
        number_of_turns = input("Entrez le nombre de tours : ")
        info_tounament.append(number_of_turns)
        players = self.add_player_to_tournament()
        info_tounament.append(players)
        time_control = input("Entrez le mode de controle du temps : ")
        info_tounament.append(time_control)
        description = input("Entrez les remarques générales : ")
        info_tounament.append(description)

        return info_tounament

    def add_player_to_tournament(self):
        players = []

        for i in range(2):
            print("Selectionnez les joueurs du tournoi : ")
            for index, player in enumerate(self.list_of_players):
                if [player, 0] not in players:
                    print(index, player)
            player_to_add = input(
                "Tapez le numero correspondant au joueur que vous voulez ajouter : "
            )
            player_selection = self.list_of_players[int(player_to_add)]
            players.append([player_selection, 0])

        return players

    def display_tournament(self, tournament):
        print("\033c")
        console.print(tournament, style="bold magenta")

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
        print("Tous les rounds ont étaient joués, le tournoi est terminé")
        print("Voici le classement final : ")
        for player in classment:
            print(
                f"{player[0].first_name} {player[0].last_name}, classement : {player[0].classment}"
            )
            print(f"Score au tournoi : {player[1]}")

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
