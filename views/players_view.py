import re
from rich.console import Console
from views.components import Components


class PlayersView(Components):
    def __init__(self):
        super().__init__()
        self.console = Console()

    def prompt_for_player(self):
        info_player = []
        print("\033c")
        self.console.print("Ajouter un joueur", style="bold red\n")
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

    def display_all_players(self, players, order):
        print("\033c")
        self.console.print(
            f"Liste de tous les joueurs par {order}: \n", style="bold red"
        )
        self.players_table(players)
        self.console.print(
            "\n1 - Joueurs par classement (défaut) \n"
            "2 - Joueurs par ordre alphabétique \n"
            "0 - Revenir au menu \n",
            style="bold magenta",
        )
        self.console.print("Que voulez-vous faire ?", style="bold red")
        user_choice = input("=> ")
        return user_choice

    def general_input(self, message):
        self.console.print(f"\n{message}", style="bold magenta")
        user_input = input("=> ")
        if user_input:
            print("\033c")
            return user_input
        else:
            self.console.print("Champs obligatoire : ", style="bold red")
            return self.general_input(message)

    def input_date_of_birth(self):
        self.console.print(
            "\nEntrez la date de naissance du joueur (jj/mm/aaaa): ",
            style="bold magenta",
        )
        date_of_birth = input("=> ")
        if date_of_birth:
            validation = re.match(
                "^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$",
                date_of_birth,
            )
            if validation:
                print("\033c")
                return date_of_birth
            else:
                self.console.print(
                    "Format de la date de naissance incorrect", style="bold red"
                )
                return self.input_date_of_birth()
        else:
            return self.input_date_of_birth()

    def input_sex(self):
        self.console.print(
            "\nEntrez le sexe du joueur (m ou f): ",
            style="bold magenta",
        )
        sex = input("=> ")
        if sex == "m" or sex == "f":
            print("\033c")
            return sex
        else:
            return self.input_sex()

    def input_classment(self):
        self.console.print(
            "\nEntrez le classement du joueur : ",
            style="bold magenta",
        )
        classment = input("=> ")
        validation = re.match("^\d+$", classment)
        if validation:
            print("\033c")
            return classment
        else:
            self.console.print("Veuillez entrer un nombre positif", style="bold red")
            return self.input_classment()

    def display_player(self, player):
        self.console.print("Nouveau joueur ajouté :", style="bold red")
        print(player)

    def prompt_add_another_player(self):
        print()
        self.console.print(
            "Voulez-vous ajouter un autre joueur ? (y/n)", style="bold red"
        )
        choice = input("=> ")
        return choice
