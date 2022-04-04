class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players 
        self.coach = coach 
        self.points = 0

    def add_player(self,new_player):
        self.players.append(new_player)

    def team_players(self):
        return len(self.players)

    def has_player(self, player_there):
        for player in self.players:
            if player == player_there:
                return True
        return False

        # answer = False
        # for player in self.players:
        #     if player == player:
        #         answer = True
        # return answer 
        
        # return self.players.count(player) > 0

    def play_game(self, game_won):
        if game_won:
            self.points += 3
            
   

Team.coach = "John Candy"