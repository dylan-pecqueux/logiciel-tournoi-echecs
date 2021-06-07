from views.players_view import PlayersView


class BaseView:

    def prompt_for_choice(self):
        print("1 - Ajouter un joueur\n"
              "2 - Voir tous les joueurs\n"
              "0 - Quitter")
        choice = input("Que voulez vous faire ? : ")
        return choice
