
class Team:
    def __init__(self, team_name):
        self.team_name: str = team_name
        self.points: int = 0
    
    def add_points(self, point):
        self.points+=point
        
    def get_team_name(self) -> str:
        return self.team_name
    
    def get_points(self) -> int:
        return self.points
    
    def __str__(self) -> str:
        return f"{self.team_name}, {self.points} pts"