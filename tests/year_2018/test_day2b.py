from src.year_2018.day2b import common_chars

def test_common_chars():
    assert common_chars(['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']) == 'fgij'
