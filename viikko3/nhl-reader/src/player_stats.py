from datetime import datetime

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader


    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        player_list = []
        for player in players:
            if player.nationality == nationality:
                player_list.append(player)

        player_list.sort(key=lambda player: player.points, reverse=True)
        print(f"Players from {nationality}: {datetime.now()}")

        return player_list
