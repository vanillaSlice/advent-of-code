#!/usr/bin/env python3

"""
Solution to problem at https://adventofcode.com/2018/day/3#part2.
"""

import os
import re

pattern = re.compile('#(?P<claim_id>\\d+) @ (?P<left>\\d+),(?P<top>\\d+): (?P<width>\\d+)x(?P<height>\\d+)')

def overlap(claims):
    claimed = [[set() for x in range(1000)] for y in range(1000)]
    no_overlaps = set()
    for claim in claims:
        claim_id, left, top, width, height = __parse_claim(claim)
        no_overlaps.add(claim_id)
        for x in range(left, left + width):
            for y in range(top, top + height):
                if claimed[x][y]:
                    no_overlaps.discard(claim_id)
                    no_overlaps -= claimed[x][y]
                claimed[x][y].add(claim_id)
    return no_overlaps.pop()

def __parse_claim(claim):
    m = pattern.match(claim)
    return int(m.group('claim_id')), \
           int(m.group('left')), \
           int(m.group('top')), \
           int(m.group('width')), \
           int(m.group('height'))

if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(__file__), 'input/day3b.txt')) as f:
        print('The answer is: {}'.format(overlap(f.read().splitlines())))
