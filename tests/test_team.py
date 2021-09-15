
from Team import Team


def test_add_points():
    team = Team("Chiefs")
    team.add_points(2)
    
    assert team.getPoints() == 2