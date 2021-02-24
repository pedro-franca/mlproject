from mlproject.distance import haversine

def test_distance():
    assert haversine(40, 2, 30, 1) != 0
