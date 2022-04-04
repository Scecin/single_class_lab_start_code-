class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players 
        self.coach = coach 

    def add_player(self,new_player):
        self.players.append(new_player)

    def team_players(self):
        return len(self.players)

    def has_player(self, name):
        answer = False
        for player in self.players:
            if player == name:
                answer = True
        return answer 
            
   

Team.coach = "John Candy"