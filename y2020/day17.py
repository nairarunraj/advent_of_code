"""
--- Day 17: Conway Cubes ---
"""

import itertools
from operator import itemgetter

from y2020.file_utils import get_input_data


def nbs4(neighbors, grid3d, loc):
    return sum(1 for d in neighbors if (loc[0] + d[0], loc[1] + d[1], loc[2] + d[2], loc[3] + d[3]) in grid3d)


def nbs3(neighbors, grid3d, loc):
    return sum(1 for d in neighbors if (loc[0] + d[0], loc[1] + d[1], loc[2] + d[2]) in grid3d)


def get_range(idx, grid3d):
    return range(min(grid3d, key=itemgetter(idx))[idx] - 1,
                 max(grid3d, key=itemgetter(idx))[idx] + 2)


def puzzle1(input_file) -> int:
    input_content = get_input_data(input_file)
    grid3d = set()

    for y, line in enumerate(input_content):
        for x, ch in enumerate(line):
            if ch == '#':
                grid3d.add((x, y, 0))

    neighbors = [coord for coord in itertools.product([-1, 0, 1], repeat=3) if
                 coord != (0, 0, 0)]

    for _ in range(6):
        grid3d_copy = set()
        range_x = get_range(0, grid3d)
        range_y = get_range(1, grid3d)
        range_z = get_range(2, grid3d)
        for coord in itertools.product(range_x, range_y, range_z):
            if coord in grid3d:
                if nbs3(neighbors, grid3d, coord) in (2, 3):
                    grid3d_copy.add(coord)
            else:
                if nbs3(neighbors, grid3d, coord) == 3:
                    grid3d_copy.add(coord)
        grid3d = grid3d_copy

    return len(grid3d)


def puzzle2(input_file) -> int:
    input_content = get_input_data(input_file)

    neighbors = [coord for coord in itertools.product([-1, 0, 1], repeat=4) if
                 coord != (0, 0, 0, 0)]

    grid4d = set()

    for y, line in enumerate(input_content):
        for x, ch in enumerate(line):
            if ch == '#':
                grid4d.add((x, y, 0, 0))

    for _ in range(6):
        grid4d_copy = set()
        range_x = get_range(0, grid4d)
        range_y = get_range(1, grid4d)
        range_z = get_range(2, grid4d)
        range_w = get_range(3, grid4d)
        for coord in itertools.product(range_x, range_y, range_z, range_w):
            if coord in grid4d:
                if nbs4(neighbors, grid4d, coord) in (2, 3):
                    grid4d_copy.add(coord)
            else:
                if nbs4(neighbors, grid4d, coord) == 3:
                    grid4d_copy.add(coord)
        grid4d = grid4d_copy

    return len(grid4d)


if __name__ == '__main__':
    answer = puzzle1("../resources/y2020/day17/day17_1.txt")
    print(answer)

    answer = puzzle1("../resources/y2020/day17/day17_2.txt")
    print(answer)

    answer = puzzle2("../resources/y2020/day17/day17_1.txt")
    print(answer)

    answer = puzzle2("../resources/y2020/day17/day17_2.txt")
    print(answer)
