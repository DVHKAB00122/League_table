
class Team:
    def __init__(self, teamName):
        self.teamName: str = teamName
        self.points: int = 0
    
    def add_points(self, point):
        self.points+=point
        
    def getTeamName(self) -> str:
        return self.teamName
    
    def getPoints(self) -> int:
        return self.points
    
    def __str__(self) -> str:
        return f"{self.teamName}, {self.points} pts"