"""
--- Day 24: Lobby Layout ---
"""
import copy
from collections import defaultdict

from y2020.file_utils import get_input_data


def get_dir(dir_map, nav, current_tile):
    return (current_tile[0] + dir_map[nav][0], current_tile[1] + dir_map[nav][1])


def puzzle1(input_file) -> int:
    input_content = get_input_data(input_file)

    tiles = set()
    start_tile = (0, 0)
    dir_map = {'nw': (0.5, 0.5), 'ne': (-0.5, 0.5), 'sw': (0.5, -0.5), 'se': (-0.5, -0.5), 'e': (-1, 0), 'w': (1, 0)}

    for line in input_content:
        path = []
        prev = ''
        for ch in line:
            if prev in ('n', 's'):
                direction = prev + ch
                prev = ''
                path.append(direction)
                continue

            if ch in ('n', 's'):
                prev = ch
                continue

            path.append(ch)

        current_tile = start_tile
        for nav in path:
            current_tile = get_dir(dir_map, nav, current_tile)

        if current_tile in tiles:
            tiles.remove(current_tile)
        else:
            tiles.add(current_tile)

    return len(tiles)


def get_neighbors(dir_map, tile):
    neighbors = set()
    for nav in dir_map.keys():
        neighbor = get_dir(dir_map, nav, tile)
        neighbors.add(neighbor)

    return neighbors


def puzzle2(input_file) -> int:
    input_content = get_input_data(input_file)

    tiles = defaultdict(bool)  # False = white, True = black
    start_tile = (0, 0)
    dir_map = {'nw': (0.5, 0.5), 'ne': (-0.5, 0.5), 'sw': (0.5, -0.5), 'se': (-0.5, -0.5), 'e': (-1, 0), 'w': (1, 0)}

    for line in input_content:
        path = []
        prev = ''
        for ch in line:
            if prev in ('n', 's'):
                direction = prev + ch
                prev = ''
                path.append(direction)
                continue

            if ch in ('n', 's'):
                prev = ch
                continue

            path.append(ch)

        current_tile = start_tile
        for nav in path:
            current_tile = get_dir(dir_map, nav, current_tile)

        tiles[current_tile] = not tiles[current_tile]

    for _ in range(100):
        new_tiles = copy.deepcopy(tiles)
        for current_tile in tiles:
            neighbors = get_neighbors(dir_map, current_tile)
            for neighbor in neighbors:
                if neighbor not in tiles:
                    new_tiles[neighbor] = False

        tiles = new_tiles

        to_be_flipped = {}
        for tile, color in tiles.items():
            neighbors = get_neighbors(dir_map, tile)
            assert len(neighbors) == 6
            black_neighbors = 0
            for neighbor in neighbors:
                if neighbor in tiles and tiles[neighbor]:
                    black_neighbors += 1

            if color:  # black
                if black_neighbors == 0 or black_neighbors > 2:
                    to_be_flipped[tile] = False
                continue

            if black_neighbors == 2:
                to_be_flipped[tile] = True

        for tile, color in to_be_flipped.items():
            tiles[tile] = color

    return list(tiles.values()).count(True)


if __name__ == '__main__':
    answer = puzzle1("../resources/y2020/day24/day24_1.txt")
    print(answer)

    answer = puzzle1("../resources/y2020/day24/day24_2.txt")
    print(answer)

    answer = puzzle2("../resources/y2020/day24/day24_1.txt")
    print(answer)

    answer = puzzle2("../resources/y2020/day24/day24_2.txt")
    print(answer)
