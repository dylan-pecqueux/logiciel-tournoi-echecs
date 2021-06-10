from controllers.player_controller import PlayerController


class TournamentView:

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

        players = input("Selectionnez les joueurs du tournoi : ")
        info_tounament.append(players)
        time_control = input("Entrez le mode de controle du temps : ")
        info_tounament.append(time_control)
        description = input("Entrez les remarques générales : ")
        info_tounament.append(description)

        return info_tounament
