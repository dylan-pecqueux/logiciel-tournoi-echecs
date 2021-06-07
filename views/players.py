class Players:

    def prompt_for_player(self):
        info_player = []

        last_name = input("Entrez le nom de famille du joueur : ")
        info_player.append(last_name)
        first_name = input("Entrez le prénom du joueur : ")
        info_player.append(first_name)
        date_of_birth = input(
            "Entrez la date de naissance du joueur (dd/mm/aaaa): ")
        info_player.append(date_of_birth)
        sex = input("Entrez le sexe du joueur (m ou f): ")
        info_player.append(sex)
        classment = input("Entrez le classement du joueur : ")
        info_player.append(classment)

        return info_player

    def display_player(self, player):
        print(player)
