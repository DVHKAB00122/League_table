from src.Team import Team
from src.TeamResult import TeamResult
from src.League import League
  
class LeagueStandings:
    
    def main():
        league: League = League()
        with open("matches.txt", "r") as file:
            for match in file:
                game = match.strip("\n").split(",")
                team_1 = game[0].split(" ") 
                team_2 = game[1].split(" ")
                team_1_game_result: TeamResult = TeamResult(Team(" ".join(team_1[0:-1])), int(team_1[-1]))
                team_2_game_result: TeamResult = TeamResult(Team(" ".join(team_2[1:-1])), int(team_2[-1]))
                
                league.game_points(team_1_game_result ,team_2_game_result)
        
        for team in league.get_standing_order_by_name():
            print(team)
    if __name__ == "__main__":
        main()