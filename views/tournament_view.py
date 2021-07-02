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
        print(tournament)

    def display_tournament_info(self, tournament):
        print(tournament)
        print("1 - Commencer le tournoi\n" "2 - Revenir au menu")
        user_choice = input("Que voulez-vous faire ? : ")
        return user_choice

    def display_tournament_end(self, classment):
        print("Tous les rounds ont étaient joués, le tournoi est terminé")
        print("Voici le classement final : ")
        for player in classment:
            print(
                f"{player[0].first_name} {player[0].last_name}, classement : {player[0].classment}"
            )
            print(f"Score au tournoi : {player[1]}")
