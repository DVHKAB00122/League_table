from TeamResult import TeamResult
from Team import Team
from typing import List

class League:
    def __init__(self):
        self.list_of_teams: List[Team] = []

    def add_team(self, team):
        self.list_of_teams.append(team)
        
    def get_list_of_teams(self) -> List[Team]:
        return self.list_of_teams
    
    def get_team_with_team_name(self, team_name) -> Team:
        for team in self.list_of_teams:
            if team.get_team_name() == team_name:
                return team
        return None
            
    def check_if_teams_exist(self, teams):
        for team in teams:
            add_new_team = True
            for existing_team in self.list_of_teams:
                if team.get_team_name() == existing_team.get_team_name():
                    add_new_team = False
            if add_new_team:
                self.add_team(team)
                    
    def get_standing_order_by_name(self) -> List[Team]:
        sort_by_name_and_points = sorted(self.get_list_of_teams(), key=lambda x: (-x.get_points(), x.get_team_name()))
        return sort_by_name_and_points
            
    def update_team_points(self, team_obj: Team, points: int):
        for team in self.list_of_teams:
            if team.get_team_name() == team_obj.get_team_name():
                team.add_points(points)
        
    def game_points(self, team_1_game: TeamResult, team_2_game: TeamResult):
        team_1: Team = team_1_game.get_team()
        team_2: Team = team_2_game.get_team()
        list_of_teams: List[Team] = [team_1, team_2]
        self.check_if_teams_exist(list_of_teams)
         
        if int(team_1_game.get_score()) == int(team_2_game.get_score()):
            self.update_team_points(team_1, 1)
            self.update_team_points(team_2, 1)
        elif int(team_1_game.get_score()) > int(team_2_game.get_score()):
            self.update_team_points(team_1, 3)
        else:
            self.update_team_points(team_2, 3)
        