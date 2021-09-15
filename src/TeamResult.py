from Team import Team

class TeamResult:
    def __init__(self, team, score):
        self.team: Team = team
        self.score: int = score
        
    def getScore(self) -> int:
        return self.score
    
    def getTeam(self) -> Team:
        return self.team
    
    def __str__(self) -> str:
        return self.getTeam().__str__() +" "+ str(self.getScore())