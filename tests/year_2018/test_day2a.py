from src.year_2018.day2a import box_checksum

def test_box_checksum():
    assert box_checksum(['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']) == 12
