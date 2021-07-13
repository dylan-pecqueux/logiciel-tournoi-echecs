from datetime import datetime
from rich.console import Console
from rich.table import Table


class NewTournamentView:
    def __init__(self, all_players):
        self.list_of_players = all_players
        self.console = Console()

    def prompt_info_tournament(self):
        info_tounament = []
        print("\033c")
        self.console.print("Création de tournoi", style="bold red\n")
        name = self.general_input("Entrez le nom du tournoi : ")
        info_tounament.append(name)
        location = self.general_input("Entrez le lieu du tournoi : ")
        info_tounament.append(location)
        start_date = self.input_start_date()
        info_tounament.append(start_date)
        end_date = self.input_end_date(start_date)
        info_tounament.append(end_date)
        players = self.add_player_to_tournament()
        info_tounament.append(players)
        print("\033c")
        time_control = self.input_time_control()
        info_tounament.append(time_control)
        description = self.general_input("Entrez les remarques générales : ")
        info_tounament.append(description)

        return info_tounament

    def add_player_to_tournament(self):
        players = []

        def selection_player():
            for i in range(2):
                print("\033c")
                self.console.print(
                    "Selectionnez les joueurs du tournoi : ", style="bold magenta"
                )
                table = Table(show_header=True, header_style="bold red")
                table.add_column("Numero", style="dim")
                table.add_column("Rank", justify="right")
                table.add_column("Nom", justify="right")
                table.add_column("Genre", justify="right")
                table.add_column("Date de naissance", justify="right")
                for index, player in enumerate(self.list_of_players):
                    if [player, 0] not in players:
                        table.add_row(
                            f"{index}",
                            f"{player.classment}",
                            f"[magenta]{player.first_name} {player.last_name}[/magenta]",
                            player.sex,
                            player.date_of_birth,
                        )
                self.console.print(table)
                self.console.print(
                    "\nEntrez le numero correspondant au joueur que vous voulez ajouter : ",
                    style="bold red",
                )
                player_to_add = input("=> ")
                player_selection = self.list_of_players[int(player_to_add)]
                players.append([player_selection, 0])
            self.console.print(
                "\nVoulez-vous ajouter encore des joueurs ? (y/n)", style="bold red"
            )
            add_player_again = input("=> ")
            if add_player_again == "y":
                selection_player()

        selection_player()
        return players

    def display_tournament_added(self):
        self.console.print("\nTournoi bien ajouté", style="bold red")
        self.console.print(
            "\nAppuyer sur entrée pour voir le tournoi ajouté", style="bold red"
        )
        input("=> ")

    def general_input(self, message):
        self.console.print(f"\n{message}", style="bold magenta")
        user_input = input("=> ")
        if user_input:
            print("\033c")
            return user_input
        else:
            self.console.print("Champs obligatoire : ", style="bold red")
            return self.general_input(message)

    def input_start_date(self):
        self.console.print("Entrez la date de début : ", style="bold magenta")
        user_input = input("=> ")
        try:
            date = datetime.strptime(user_input, "%d/%m/%Y")
            if date > date.now():
                print("\033c")
                return date
            else:
                self.console.print(
                    "\nVeuillez entrer une date future\n", style="bold red"
                )
                return self.input_start_date()
        except:
            self.console.print("\nFormat invalide\n", style="bold red")
            self.input_start_date()

    def input_end_date(self, start_date):
        self.console.print("Entrez la date de fin : ", style="bold magenta")
        user_input = input("=> ")
        try:
            date = datetime.strptime(user_input, "%d/%m/%Y")
            if date >= start_date:
                print("\033c")
                return date
            else:
                self.console.print(
                    "\nVeuillez entrer une date supérieur ou égal à la date de début du tournoi\n",
                    style="bold red",
                )
                return self.input_end_date(start_date)
        except:
            self.console.print("\nFormat invalide\n", style="bold red")
            self.input_end_date(start_date)

    def input_time_control(self):
        self.console.print(
            "Choisissez le mode de controle du temps : \n"
            "\n1 - Bullet"
            "\n2 - Blitz"
            "\n3 - Coup rapide",
            style="bold magenta",
        )
        user_input = input("=> ")
        if user_input == "1":
            print("\033c")
            return "Bullet"
        elif user_input == "2":
            print("\033c")
            return "Blitz"
        elif user_input == "3":
            print("\033c")
            return "Coup rapide"
        else:
            self.console.print(
                "\nVeuillez rentrer un numéro correspondant aux choix presentés\n",
                style="bold red",
            )
            return self.input_time_control()
