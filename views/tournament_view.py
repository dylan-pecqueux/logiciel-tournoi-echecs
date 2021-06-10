from controllers.player_controller import PlayerController


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
        players = []
        for number in range(2):
            player = self.add_player_to_tournament()
            players.append(player)
        info_tounament.append(players)
        time_control = input("Entrez le mode de controle du temps : ")
        info_tounament.append(time_control)
        description = input("Entrez les remarques générales : ")
        info_tounament.append(description)

        return info_tounament

    def add_player_to_tournament(self):

        print("Selectionnez les joueurs du tournoi : ")
        for index, player in enumerate(self.list_of_players):
            print(index, player)
        player_to_add = input(
            "Tapez le numero correspondant au joueur que vous voulez ajouter : ")
        player_selection = self.list_of_players[int(player_to_add)]
        self.list_of_players.remove(player_selection)
        return player_selection

    def display_tournament(self, tournament):
        print(tournament)
