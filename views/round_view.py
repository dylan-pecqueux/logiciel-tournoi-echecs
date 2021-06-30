class RoundView:

    def display_all_matchs(self, matchs):
        for index, match in enumerate(matchs):
            print(index, match)
        end_of_round = input(
            'Entrez "y" quand le round est terminer, pour passer à la notation des scores : ')
        return end_of_round
    
    def input_score(self, matchs):
        for index, match in enumerate(matchs):
            print(f"{index} - Entrez les résultats du match {match}")
            result_player1 = input(f"Score du joueur {match.first_player[0].first_name}")
            match.first_player[1] = result_player1
            result_player2 = input(f"Score du joueur {match.second_player[0].first_name}")
            match.second_player[1] = result_player2

