
from TeamResult import TeamResult
from Team import Team
from League import League


def test_add_team():
    league = League()
    team = Team("Chiefs")
    league.add_new_teams([team])
    
    assert len(league.get_list_of_teams()) == 1

def test_add_existing_team():
    league = League()
    team = Team("Chiefs")
    league.add_new_teams([team, team])
    
    assert len(league.get_list_of_teams()) == 1
    
def test_get_team_name_that_doesnt_exists():
    league = League()

    assert league.get_team_by_team_name("Test") == None
    
    
def test_update_team_points():
    league = League()
    team = Team("Chiefs")
    
    league.add_new_teams([team])
    league.update_team_points(team,12)
    
    assert league.get_team_by_team_name("Chiefs").get_points() == 12
    
def test_allocate_game_points_to_team_1():
    league = League()
    team1 = Team("Chiefs")
    team2 = Team("Pirates")
    team1Result = TeamResult(team1, 2)
    team2Result = TeamResult(team2, 4)
    
    league.allocate_game_points(team1Result,team2Result)
    
    assert len(league.get_list_of_teams()) == 2
    assert league.get_team_by_team_name("Chiefs").get_points() == 0
    assert league.get_team_by_team_name("Pirates").get_points() == 3
    

def test_allocate_game_points_to_team_2():
    league = League()
    team1 = Team("Chiefs")
    team2 = Team("Pirates")
    team1Result = TeamResult(team1, 5)
    team2Result = TeamResult(team2, 4)
    
    league.allocate_game_points(team1Result,team2Result)
    
    assert len(league.get_list_of_teams()) == 2
    assert league.get_team_by_team_name("Chiefs").get_points() == 3
    assert league.get_team_by_team_name("Pirates").get_points() == 0
    

def test_allocate_game_points_to_both_team_():
    league = League()
    team1 = Team("Chiefs")
    team2 = Team("Pirates")
    team1Result = TeamResult(team1, 1)
    team2Result = TeamResult(team2, 1)
    
    league.allocate_game_points(team1Result,team2Result)
    
    assert len(league.get_list_of_teams()) == 2
    assert league.get_team_by_team_name("Chiefs").get_points() == 1
    assert league.get_team_by_team_name("Pirates").get_points() == 1
    

    
def test_get_league_standing():
    league = League()
    team1 = Team("Chiefs")
    team2 = Team("Pirates")
    league.add_new_teams([team1, team2])
    league.update_team_points(team2,12)
    
    assert league.get_sorted_list_of_teams()[0].get_team_name() == "Pirates"