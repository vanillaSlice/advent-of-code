from src.year_2018.day1b import chronal_calibration

def test_chronal_calibration():
    assert chronal_calibration(['+1', '-1']) == 0
    assert chronal_calibration(['+3', '+3', '+4', '-2', '-4']) == 10
    assert chronal_calibration(['-6', '+3', '+8', '+5', '-6']) == 5
    assert chronal_calibration(['+7', '+7', '-2', '-7', '-4']) == 14
