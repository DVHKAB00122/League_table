from Team import Team
from TeamResult import TeamResult
from League import League
from typing import List
  
class LeagueStandings:
    
    def main():
        league: League = League()
        with open("matches.txt", "r") as file:
            
            for match in file:
                game = match.strip("\n").split(",")
                team1 = game[0].split(" ") 
                team2 = game[1].split(" ")
                team1GameResult: TeamResult = TeamResult(Team(" ".join(team1[0:-1])), int(team1[-1]))
                team2GameResult: TeamResult = TeamResult(Team(" ".join(team2[1:-1])), int(team2[-1]))
                
                league.gamePoints(team1GameResult ,team2GameResult)
        
        for team in league.getStandingOrderByName():
            print(team)
    if __name__ == "__main__":
        main()