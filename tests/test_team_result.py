from src.TeamResult import TeamResult
from src.Team import Team


def test_get_team_result():
    team = Team("Chiefs")
    teamResult = TeamResult(team, 2)
    
    assert teamResult.get_score() == 2
    assert teamResult.get_team().get_team_name() == "Chiefs"
    assert teamResult.__str__() == "Chiefs, 0 pts 2"
