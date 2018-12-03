from src.year_2018.day3b import overlap

def test_overlap():
    assert overlap(['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']) == 3
