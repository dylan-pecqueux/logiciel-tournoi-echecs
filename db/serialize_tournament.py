class SerializeTournament:
    def serialized_tournament(self, tournament):
        serialized_tournament = {
            "name": tournament.name,
            "location": tournament.location,
            "start_date": tournament.start_date.strftime("%d/%m/%Y"),
            "end_date": tournament.end_date.strftime("%d/%m/%Y"),
            "number_of_turns": tournament.number_of_turns,
            "players_list": self.get_players_id(tournament.players_list),
            "time_control": tournament.time_control,
            "description": tournament.description,
            "rounds": self.serialized_rounds(tournament.rounds),
        }
        return serialized_tournament

    def serialized_rounds(self, rounds):
        serialized_rounds = []
        if rounds:
            for round in rounds:
                serialized_round = {
                    "all_matchs": self.serialized_matches(round.all_matchs),
                    "round_number": round.round_number,
                    "start_date": round.start_date.strftime("%d/%m/%Y, %H:%M:%S"),
                    "end_date": round.end_date.strftime("%d/%m/%Y, %H:%M:%S"),
                }
                serialized_rounds.append(serialized_round)
            return serialized_rounds
        else:
            return []

    def serialized_matches(self, matches):
        serialized_matches = []
        for match in matches:
            (match,) = match
            serialized_match = {
                "first_player": [match.first_player[0].id, match.first_player[1]],
                "second_player": [match.second_player[0].id, match.second_player[1]],
            }
            serialized_matches.append(serialized_match)
        return serialized_matches

    def get_players_id(self, players):
        players_list = []
        for player in players:
            player_inst = player[0]
            player_score = player[1]
            players_list.append([player_inst.id, player_score])
        return players_list
