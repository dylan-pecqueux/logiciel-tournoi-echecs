from rich.console import Console
from rich.table import Table
import re

console = Console()


class PlayersView:
    def prompt_for_player(self):
        info_player = []

        last_name = self.general_input("Entrez le nom de famille du joueur : ")
        info_player.append(last_name)
        first_name = self.general_input("Entrez le prénom du joueur : ")
        info_player.append(first_name)
        date_of_birth = self.input_date_of_birth()
        info_player.append(date_of_birth)
        sex = self.input_sex()
        info_player.append(sex)
        classment = self.input_classment()
        info_player.append(classment)

        return info_player

    def display_all_players(self, players):
        print("\033c")
        console.print("Liste de tous les joueurs : \n", style="bold red")
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
        console.print(table)

    def general_input(self, message):
        user_input = input(message)
        if user_input:
            return user_input
        else:
            print("Champs obligatoire :")
            return self.general_input(message)

    def input_date_of_birth(self):
        date_of_birth = input("Entrez la date de naissance du joueur (jj/mm/aaaa): ")
        if date_of_birth:
            validation = re.match(
                "^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$",
                date_of_birth,
            )
            if validation:
                return date_of_birth
            else:
                print("Format de la date de naissance incorrect")
                return self.input_date_of_birth()
        else:
            return self.input_date_of_birth()

    def input_sex(self):
        sex = input("Entrez le sexe du joueur (m ou f): ")
        if sex == "m" or sex == "f":
            return sex
        else:
            return self.input_sex()

    def input_classment(self):
        classment = input("Entrez le classement du joueur : ")
        validation = re.match("^\d+$", classment)
        if validation:
            return classment
        else:
            print("Veuillez entrer un nombre positif")
            return self.input_classment()

    def display_player(self, player):
        print(player)

    def prompt_add_another_player(self):
        print()
        print("Voulez-vous ajouter un autre joueur ?")
        choice = input("y/n ? ")
        return choice
