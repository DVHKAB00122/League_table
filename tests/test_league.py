
from TeamResult import TeamResult
from Team import Team
from League import League


def test_add_team():
    league = League()
    team = Team("Chiefs")
    
    league.addTeam(team)
    
    assert len(league.getListOfTeams()) == 1
    
    
def test_update_team_points():
    league = League()
    team = Team("Chiefs")
    
    league.addTeam(team)
    league.updateTeamPoints(team,12)
    
    assert league.getTeamWithTeamName("Chiefs").getPoints() == 12
    
def test_game_points():
    league = League()
    team1 = Team("Chiefs")
    team2 = Team("Pirates")
    team1Result = TeamResult(team1, 2)
    team2Result = TeamResult(team2, 4)
    
    league.gamePoints(team1Result,team2Result)
    
    assert len(league.getListOfTeams()) == 2
    assert league.getTeamWithTeamName("Chiefs").getPoints() == 0
    assert league.getTeamWithTeamName("Pirates").getPoints() == 3
    
def test_get_league_standing():
    league = League()
    team1 = Team("Chiefs")
    team2 = Team("Pirates")
    league.addTeam(team1)
    league.addTeam(team2)
    league.updateTeamPoints(team1,12)
    
    assert league.getStandingOrderByName() == [ team2, team1]
    
    
    
    
    
    
    
    