from TeamResult import TeamResult
from Team import Team

def test_get_team_result():
    team = Team("Chiefs")
    teamResult = TeamResult(team, 2)
    
    assert teamResult.getScore() == 2
    assert teamResult.getTeam("Chiefs")
    assert teamResult.__str__() == "Chiefs, 0 pts, 2"
