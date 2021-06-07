from views.players import Players


class View:

    def prompt_for_choice(self):
        print("1 - Ajouter un joueur\n"
              "0 - Quitter")
        choice = input("Que voulez vous faire ? : ")
        return choice
