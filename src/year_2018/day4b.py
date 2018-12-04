#!/usr/bin/env python3

"""
Solution to problem at https://adventofcode.com/2018/day/4#part2.
"""

from collections import defaultdict
from datetime import datetime
import os
import re

pattern = re.compile('\\[(?P<timestamp>\\d+\\-\\d+\\-\\d+ \\d+:\\d+)\\] (?P<message>.+)')

def repose_record(records):
    guard_slept_most = 0
    minute_slept_most = 0

    slept = {}

    current_guard = 0
    started_sleeping = 0

    for timestamp, message in sorted(parse_records(records).items()):
        current_minute = timestamp.minute

        if message == 'falls asleep':
            started_sleeping = current_minute
        elif message == 'wakes up':
            for i in range(started_sleeping, current_minute):
                if i not in slept:
                    slept[i] = defaultdict(int)
                slept[i][current_guard] += 1
        else:
            current_guard = message.split(' ')[1][1:]


    max_count = 0

    for i, guards in slept.items():
        for guard, guard_count in guards.items():
            if guard_count > max_count:
                max_count = guard_count
                guard_slept_most = guard
                minute_slept_most = i

    return int(guard_slept_most) * minute_slept_most

def parse_records(records):
    parsed_records = {}
    for record in records:
        m = pattern.match(record)
        timestamp = datetime.strptime(m.group('timestamp'), '%Y-%m-%d %H:%M')
        message = m.group('message')
        parsed_records[timestamp] = message
    return parsed_records

if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(__file__), 'input/day4b.txt')) as f:
        # 32070
        print('The answer is: {}'.format(repose_record(f.read().splitlines())))
