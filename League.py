from TeamResult import TeamResult
from Team import Team
from typing import List

class League:
    def __init__(self):
        self.list_of_teams: List[Team] = []
        
    def get_list_of_teams(self) -> List[Team]:
        return self.list_of_teams
    
    def get_team_by_team_name(self, team_name: str) -> Team:
        for team in self.list_of_teams:
            if team.get_team_name() == team_name:
                return team
        return None
            
    def add_new_teams(self, teams: List[Team]):
        for team in teams:
            add_new_team = True
            for existing_team in self.list_of_teams:
                if team.get_team_name() == existing_team.get_team_name():
                    add_new_team = False
            if add_new_team:
                self.list_of_teams.append(team)
                    
    def get_sorted_list_of_teams(self) -> List[Team]:
        sorted_list_of_teams = sorted(self.get_list_of_teams(), key=lambda x: (-x.get_points(), x.get_team_name()))
        return sorted_list_of_teams
            
    def update_team_points(self, team_obj: Team, points: int):
        for team in self.list_of_teams:
            if team.get_team_name() == team_obj.get_team_name():
                team.add_points(points)
        
    def allocate_game_points(self, team_1_game: TeamResult, team_2_game: TeamResult):
        team_1: Team = team_1_game.get_team()
        team_2: Team = team_2_game.get_team()
        list_of_teams: List[Team] = [team_1, team_2]
        self.add_new_teams(list_of_teams)
         
        if int(team_1_game.get_score()) == int(team_2_game.get_score()):
            self.update_team_points(team_1, 1)
            self.update_team_points(team_2, 1)
        elif int(team_1_game.get_score()) > int(team_2_game.get_score()):
            self.update_team_points(team_1, 3)
        else:
            self.update_team_points(team_2, 3)
        