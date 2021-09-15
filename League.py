from TeamResult import TeamResult
from Team import Team
from typing import List

class League:
    def __init__(self):
        self.list_of_teams: List[Team] = []

    def addTeam(self, team):
        self.list_of_teams.append(team)
        
    def getListOfTeams(self) -> List[Team]:
        return self.list_of_teams
    
    def getTeamWithTeamName(self, teamName) -> Team:
        for team in self.list_of_teams:
            if team.getTeamName() == teamName:
                return team
        return None
            
    def checkIfTeamsExist(self, teams):
        for team in teams:
            addNewTeam = True
            for existingTeam in self.list_of_teams:
                if team.getTeamName() == existingTeam.getTeamName():
                    addNewTeam = False
            if addNewTeam:
                self.addTeam(team)
                    
    def getStandingOrderByName(self):
        sortByNameAndPoints = sorted(self.getListOfTeams(), key=lambda x: (x.getPoints(), x.getTeamName()),reverse=True)
        for team in sortByNameAndPoints:
            print(team)
            
    def updateTeamPoints(self, teamObj: Team, points: int):
        for team in self.list_of_teams:
            if team.getTeamName() == teamObj.getTeamName():
                team.add_points(points)
        
    def gamePoints(self, team1Game: TeamResult, team2Game: TeamResult):
        team1: Team = team1Game.getTeam()
        team2: Team = team2Game.getTeam()
        list_of_teams: List[Team] = [team1, team2]
        self.checkIfTeamsExist(list_of_teams)
         
        if int(team1Game.getScore()) == int(team2Game.getScore()):
            self.updateTeamPoints(team1, 1)
            self.updateTeamPoints(team2, 1)
        elif int(team1Game.getScore()) > int(team2Game.getScore()):
            self.updateTeamPoints(team1, 3)
        else:
            self.updateTeamPoints(team2, 3)
        