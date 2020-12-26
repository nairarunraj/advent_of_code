"""
--- Day 13: Shuttle Search ---
"""

import math

from y2020.file_utils import get_input_data


def puzzle1(input_file) -> int:
    input_content = get_input_data(input_file)
    time_start = int(input_content[0])
    bus_ids = [int(id) for id in input_content[1].split(',') if id.isdigit()]

    min_wait_time = math.inf
    bus_to_catch = 0
    for bus_id in bus_ids:
        wait_time = (-1 * time_start) % bus_id

        if min_wait_time > wait_time:
            min_wait_time = wait_time
            bus_to_catch = bus_id

    return min_wait_time * bus_to_catch


def puzzle2(input_file) -> int:
    input_content = get_input_data(input_file)

    bus_ids = ['x' if bus_id == 'x' else int(bus_id) for bus_id in input_content[1].split(',')]

    buses = {bus_id: -idx % bus_id for idx, bus_id in enumerate(bus_ids) if bus_id != 'x'}

    sorted_ids = list(reversed(sorted(buses)))
    timestamp = buses[sorted_ids[0]]
    multiplier = sorted_ids[0]
    for bus_id in sorted_ids[1:]:
        while timestamp % bus_id != buses[bus_id]:
            timestamp += multiplier

        multiplier *= bus_id

    return timestamp


if __name__ == '__main__':
    answer = puzzle1("../../resources/y2020/day13/day13_1.txt")
    print(answer)

    answer = puzzle1("../../resources/y2020/day13/day13_2.txt")
    print(answer)

    answer = puzzle2("../../resources/y2020/day13/day13_1.txt")
    print(answer)

    answer = puzzle2("../../resources/y2020/day13/day13_2.txt")
    print(answer)
