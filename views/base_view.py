from rich.console import Console


class BaseView:
    def __init__(self):
        self.console = Console()

    def welcome(self):
        self.console.print(
            "_________ .__                     __   \n"
            "\_   ___ \|  |__   ____   _______/  |_ \n"
            "/    \  \/|  |  \_/ __ \ /  ___/\   __\ \n"
            "\     \___|   Y  \  ___/ \___ \  |  |  \n"
            " \______  /___|  /\___  >____  > |__|  \n"
            "        \/     \/     \/     \/        \n",
            style="bold red",
        )
        self.console.print(
            "___________                                                      __   \n"
            "\__    ___/___  __ _________  ____ _____    _____   ____   _____/  |_ \n"
            "  |    | /  _ \|  |  \_  __ \/    \\__  \  /     \_/ __ \ /    \   __\ \n"
            "  |    |(  <_> )  |  /|  | \/   |  \/ __ \|  Y Y  \  ___/|   |  \  |  \n"
            "  |____| \____/|____/ |__|  |___|  (____  /__|_|  /\___  >___|  /__|  \n"
            "                                 \/     \/      \/     \/     \/      \n",
            style="bold red",
        )

    def prompt_for_choice(self):
        print("\033c")
        self.welcome()
        self.console.print(
            "\n1 - Ajouter un joueur\n"
            "2 - Voir tous les joueurs\n"
            "3 - Créer un tournoi\n"
            "4 - Voir tous les tournois\n"
            "0 - Quitter\n ",
            style="bold magenta",
        )
        self.console.print("Que voulez vous faire ? : ", style="bold red")
        choice = input("")
        return choice
