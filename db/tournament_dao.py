from db.abstract_dao import AbstractDAO
from models.tournament import Tournament


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
        }
        return serialized_tournament

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
            self.add_tournament(load_tournament)

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
