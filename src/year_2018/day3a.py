#!/usr/bin/env python3

"""
Solution to problem at https://adventofcode.com/2018/day/3.
"""

import os
import re

pattern = re.compile('#(?P<id>\\d+) @ (?P<left>\\d+),(?P<top>\\d+): (?P<width>\\d+)x(?P<height>\\d+)')

def overlap(claims):
    claimed = [[0 for x in range(1000)] for y in range(1000)]
    overlaps = 0
    for claim in map(__parse_claim, claims):
        for x in range(claim['left'], claim['left'] + claim['width']):
            for y in range(claim['top'], claim['top'] + claim['height']):
                claimed[x][y] = claimed[x][y] + 1
                if claimed[x][y] == 2:
                    overlaps += 1
    return overlaps

def __parse_claim(claim):
    m = pattern.match(claim)
    return {
        '_id': int(m.group('id')),
        'left': int(m.group('left')),
        'top': int(m.group('top')),
        'width': int(m.group('width')),
        'height': int(m.group('height'))
    }

if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(__file__), 'input/day3a.txt')) as f:
        print('The answer is: {}'.format(overlap(f.read().splitlines())))
