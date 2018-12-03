#!/usr/bin/env python3

"""
Solution to problem at https://adventofcode.com/2018/day/3#part2.
"""

import os
import re

pattern = re.compile('#(?P<id>\\d+) @ (?P<left>\\d+),(?P<top>\\d+): (?P<width>\\d+)x(?P<height>\\d+)')

def overlap(claims):
    claimed = [[set() for x in range(1000)] for y in range(1000)]
    no_overlaps = set()
    for claim in map(__parse_claim, claims):
        no_overlaps.add(claim['_id'])
        for x in range(claim['left'], claim['left'] + claim['width']):
            for y in range(claim['top'], claim['top'] + claim['height']):
                if claimed[x][y]:
                    no_overlaps.discard(claim['_id'])
                    no_overlaps -= claimed[x][y]
                claimed[x][y].add(claim['_id'])
    return no_overlaps.pop()

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
    with open(os.path.join(os.path.dirname(__file__), 'input/day3b.txt')) as f:
        print('The answer is: {}'.format(overlap(f.read().splitlines())))
