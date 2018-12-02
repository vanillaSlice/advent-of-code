from src.year_2018.day1b import chronal_calibration

def test_chronal_calibration_1():
    assert chronal_calibration(['+1', '-1']) == 0

def test_chronal_calibration_2():
    assert chronal_calibration(['+3', '+3', '+4', '-2', '-4']) == 10

def test_chronal_calibration_3():
    assert chronal_calibration(['-6', '+3', '+8', '+5', '-6']) == 5

def test_chronal_calibration_4():        
    assert chronal_calibration(['+7', '+7', '-2', '-7', '-4']) == 14
