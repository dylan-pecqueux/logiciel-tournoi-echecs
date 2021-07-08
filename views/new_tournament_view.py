from rich.console import Console

console = Console()


class NewTournamentView:
    def prompt_info_tournament(self):
        info_tounament = []
        print("\033c")
        console.print("Création de tournoi", style="bold red\n")
        console.print("\nEntrez le nom du tournoi : ", style="bold magenta")
        name = input("=> ")
        info_tounament.append(name)
        print("\033c")
        console.print("Entrez le lieu du tournoi : ", style="bold magenta")
        location = input("=> ")
        info_tounament.append(location)
        print("\033c")
        console.print("Entrez la date de début : ", style="bold magenta")
        start_date = input("=> ")
        info_tounament.append(start_date)
        print("\033c")
        console.print("Entrez la date de fin : ", style="bold magenta")
        end_date = input("=> ")
        info_tounament.append(end_date)
        print("\033c")
        players = self.add_player_to_tournament()
        info_tounament.append(players)
        print("\033c")
        console.print("Entrez le mode de controle du temps : ", style="bold magenta")
        time_control = input("=> ")
        info_tounament.append(time_control)
        print("\033c")
        console.print("Entrez les remarques générales : ", style="bold magenta")
        description = input("=> ")
        info_tounament.append(description)
        print("\033c")

        return info_tounament

    def add_player_to_tournament(self):
        players = []

        def selection_player():
            for i in range(2):
                print("\033c")
                console.print(
                    "Selectionnez les joueurs du tournoi : ", style="bold magenta"
                )
                for index, player in enumerate(self.list_of_players):
                    if [player, 0] not in players:
                        print(index, player)
                console.print(
                    "\nEntrez le numero correspondant au joueur que vous voulez ajouter : ",
                    style="bold red",
                )
                player_to_add = input("=> ")
                player_selection = self.list_of_players[int(player_to_add)]
                players.append([player_selection, 0])
            console.print(
                "\nVoulez-vous ajouter encore des joueurs ? (y/n)", style="bold red"
            )
            add_player_again = input("=> ")
            if add_player_again == "y":
                selection_player()

        return players
