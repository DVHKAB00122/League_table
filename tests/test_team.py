


from Team import Team


# def test_add_points():
#     team = Team("Chiefs")
#     team.add_points(2)
    
#     assert team.getPoints() == 2
    
def test_get_team_name():
    team = Team("Chiefs")
    
    assert team.getTeamName() == "Chiefs"
    assert team.__str__() == "Chiefs, 0 pts"
    
    
    