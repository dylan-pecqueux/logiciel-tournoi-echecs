import re


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
        print("\n Liste de tous les joueurs : \n")
        for player in players:
            print(f"{player}\n")

    def general_input(self, message):
        user_input = input(message)
        if user_input:
            return user_input
        else:
            print("Champs obligatoire :")
            return self.general_input(message)

    def input_date_of_birth(self):
        date_of_birth = input(
            "Entrez la date de naissance du joueur (jj/mm/aaaa): ")
        if date_of_birth:
            validation = re.match(
                '^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$', date_of_birth)
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
        validation = re.match('^\d+$', classment)
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
