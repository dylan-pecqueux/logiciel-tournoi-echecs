class RoundView:
    def display_all_matchs(self, matchs):
        for index, match in enumerate(matchs):
            print(index, match)
        end_of_round = input(
            'Entrez "y" quand le round est terminer, pour passer à la notation des scores : '
        )
        return end_of_round

    def input_score(self, match):
        print(f"Entrez les résultats du match {match}")
        print(f"1 - {match.first_player[0].first_name}")
        print(f"2 - {match.second_player[0].first_name}")
        winner = input('Entrez le numéro du joueur gagnant ou "eg" en cas de match nul')
        return winner

    def display_classment_players(self, players):
        for player in players:
            print(
                f"{player[0].first_name} {player[0].last_name}, classement : {player[0].classment}"
            )
            print(f"Score au tournoi : {player[1]}")
