class TournamentsView:

    def display_all_tournaments(self, tournaments):
        for index, tournament in enumerate(tournaments):
            print(f"{index} - {tournament.name_and_date()}")
        print("0 - Revenir au menu")
        user_choice = input(
            "Tapez le numéro du tournoi que vous voulez voir : ")
        return user_choice
