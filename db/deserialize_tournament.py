from models.tournament import Tournament
from models.round import Round
from models.match import Match


class DeserializeTournament:
    def __init__(self, all_players):
        self.all_players = all_players

    def deserialized_tournaments(self, tournaments):
        loaded_tournaments = []
        for tournament in tournaments:
            name = tournament["name"]
            location = tournament["location"]
            start_date = tournament["start_date"]
            end_date = tournament["end_date"]
            number_of_turns = tournament["number_of_turns"]
            time_control = tournament["time_control"]
            description = tournament["description"]
            players_list = self.get_players_of_tournament(tournament["players_list"])
            id = tournament.doc_id
            load_tournament = Tournament(
                name,
                location,
                start_date,
                end_date,
                number_of_turns,
                players_list,
                time_control,
                description,
                id,
            )
            if tournament["rounds"]:
                rounds = self.deserialized_rounds(tournament["rounds"], load_tournament)
                load_tournament.rounds = rounds
            loaded_tournaments.append(load_tournament)
        return loaded_tournaments

    def deserialized_rounds(self, rounds, tournament):
        deserialized_rounds = []
        if rounds:
            for round in rounds:
                round_number = round["round_number"]
                start_date = round["start_date"]
                end_date = round["end_date"]
                load_round = Round(round_number, start_date, end_date)
                all_matches = self.deserialized_matches(round["all_matchs"], tournament)
                load_round.all_matchs = all_matches
                deserialized_rounds.append(load_round)
            return deserialized_rounds
        else:
            return []

    def deserialized_matches(self, matches, tournament):
        deserialized_matches = []
        for match in matches:
            first_player_inst = self.find_player(match["first_player"][0])
            first_player_score = match["first_player"][1]
            second_player_inst = self.find_player(match["second_player"][0])
            second_player_score = match["second_player"][1]
            load_match = Match(
                first_player_inst,
                second_player_inst,
                tournament,
                first_player_score,
                second_player_score,
            )
            deserialized_matches.append(load_match)
        return deserialized_matches

    def get_players_of_tournament(self, players_list):
        players = []
        for player in players_list:

            player_id = player[0]
            player_score = player[1]
            find_player = self.find_player(player_id)
            players.append([find_player, player_score])
        return players

    def find_player(self, player_to_find):
        all_players = self.all_players
        for player in all_players:
            if player.id == player_to_find:
                return player
