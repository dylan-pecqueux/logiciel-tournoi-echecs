from db.abstract_dao import AbstractDAO
from models.tournament import Tournament
from models.round import Round
from models.match import Match


class TournamentDAO(AbstractDAO):
    def __init__(self, all_players):
        super().__init__()
        self.all_players = all_players

    def save(self, tournament):
        serialized_tournament = self.serialized_tournament(tournament)
        self.db.save_tournament(serialized_tournament)
        self.add_tournament(tournament)

    def serialized_tournament(self, tournament):
        serialized_tournament = {
            "name": tournament.name,
            "location": tournament.location,
            "start_date": tournament.start_date,
            "end_date": tournament.end_date,
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
                }
                serialized_rounds.append(serialized_round)
            return serialized_rounds
        else:
            return []

    def serialized_matches(self, matches):
        serialized_matches = []
        for match in matches:
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

    def all_tournaments(self):
        return self.db.all_tournaments()

    def add_tournament(self, tournament):
        self.db.add_tournament(tournament)

    def get_tournaments(self):
        return self.db.tournaments

    def deserialized_tournaments(self):
        tournaments = self.all_tournaments()
        for tournament in tournaments:
            name = tournament["name"]
            location = tournament["location"]
            start_date = tournament["start_date"]
            end_date = tournament["end_date"]
            number_of_turns = tournament["number_of_turns"]
            time_control = tournament["time_control"]
            description = tournament["description"]
            players_list = self.get_players_of_tournament(tournament["players_list"])
            load_tournament = Tournament(
                name,
                location,
                start_date,
                end_date,
                number_of_turns,
                players_list,
                time_control,
                description,
            )
            if tournament["rounds"]:
                rounds = self.deserialized_rounds(tournament["rounds"], load_tournament)
                load_tournament.rounds = rounds
            self.add_tournament(load_tournament)

    def deserialized_rounds(self, rounds, tournament):
        deserialized_rounds = []
        if rounds:
            for round in rounds:
                round_number = round["round_number"]
                load_round = Round(round_number)
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
