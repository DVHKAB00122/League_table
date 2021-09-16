from Team import Team

class TeamResult:
    def __init__(self, team, score):
        self.team: Team = team
        self.score: int = score
        
    def get_score(self) -> int:
        return self.score
    
    def get_team(self) -> Team:
        return self.team
    
    def __str__(self) -> str:
        return self.get_team().__str__() +" "+ str(self.get_score())