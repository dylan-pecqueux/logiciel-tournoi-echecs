class RoundView:

    def display_all_matchs(self, matchs):
        for index, match in enumerate(matchs):
            print(index, match)
        end_of_round = input(
            'Entrez "y" quand le round est terminer, pour passer à la notation des scores : ')
        return end_of_round
