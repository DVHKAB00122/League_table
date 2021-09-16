from TeamResult import TeamResult
from Team import Team
from League import League

def test_add_team():
    league = League()
    team = Team("Chiefs")
    league.add_team(team)
    
    assert len(league.get_list_of_teams()) == 1
    
    
def test_update_team_points():
    league = League()
    team = Team("Chiefs")
    
    league.add_team(team)
    league.update_team_points(team,12)
    
    assert league.get_team_with_team_name("Chiefs").get_points() == 12
    
def test_game_points():
    league = League()
    team1 = Team("Chiefs")
    team2 = Team("Pirates")
    team1Result = TeamResult(team1, 2)
    team2Result = TeamResult(team2, 4)
    
    league.game_points(team1Result,team2Result)
    
    assert len(league.get_list_of_teams()) == 2
    assert league.get_team_with_team_name("Chiefs").get_points() == 0
    assert league.get_team_with_team_name("Pirates").get_points() == 3
    
def test_get_league_standing():
    league = League()
    team1 = Team("Chiefs")
    team2 = Team("Pirates")
    league.add_team(team1)
    league.add_team(team2)
    league.update_team_points(team2,12)
    
    assert league.get_standing_order_by_name()[0].get_team_name() == "Pirates"
    
    
    
    
    
    
    
    