"""
--- Day 20: Jurassic Jigsaw ---
"""
import math
from collections import defaultdict
from copy import deepcopy

from y2020.file_utils import get_input_data


def parse_input(input_content):
    rows = columns = 0

    tiles = {}
    layout = []
    tile_no = 0
    for line in input_content:
        if 'Tile' in line:
            tile_no = line[5:-1]
        elif line == '':
            tiles[tile_no] = layout
            layout = []
        else:
            layout.append(list(line))

        if rows == 0:
            rows = columns = len(line)

    tiles[tile_no] = layout

    tile_borders = {}
    for tile_no, tile_info in tiles.items():
        for idx, tile_row in enumerate(tile_info):
            if idx == 0:
                top = tile_row
                left = [None] * columns
                right = [None] * columns

            if idx == rows - 1:
                bottom = tile_row

            left[idx] = tile_row[0]
            right[idx] = tile_row[-1]

        borders = [tuple(border) for border in [left, top, right, bottom]]
        reversed_borders = [tuple(reversed(border)) for border in borders]

        tile_borders[tile_no] = set(borders + reversed_borders)

    return tiles, tile_borders, rows, columns


def puzzle1(input_file) -> int:
    input_content = get_input_data(input_file)

    (tiles, tile_borders, rows, columns) = parse_input(input_content)

    product = 1
    for tile_no1, borders1 in tile_borders.items():
        adjacent_tiles = []
        for tile_no2, borders2 in tile_borders.items():
            if tile_no1 == tile_no2:
                continue

            if borders1 & borders2:
                adjacent_tiles.append(tile_no2)

        if len(adjacent_tiles) == 2:
            product *= int(tile_no1)

    return product


def rotate(T):
    TR = len(T)
    TC = len(T[0])
    # takes (r,c) to (c, R-1-r)
    RET = [['?' for _ in range(TR)] for _ in range(TC)]
    for r in range(TR):
        for c in range(TC):
            RET[c][TR - 1 - r] = T[r][c]
    return RET


def flip(T):
    return list(reversed(T))


def poss(T):
    ans = set()
    flips = [deepcopy(T), flip(T)]
    for _ in range(4):
        for i in range(len(flips)):
            ans.add(tuple([tuple(row) for row in flips[i]]))
            flips[i] = rotate(flips[i])

    return ans


# Does the boundary of p1 match p2, assuming p2 is in the direction (dr,dc)?
def matches(rows, columns, p1, p2, dr, dc):
    if dr == -1:  # up, so top of p1 should match bottom of p2
        for c in range(columns):
            if p1[0][c] != p2[rows - 1][c]:
                return False
        return True
    elif dc == 1:  # right, so right of p1 should match left of p2
        for r in range(rows):
            if p1[r][columns - 1] != p2[r][0]:
                return False
        return True
    elif dr == 1:  # bottom
        for c in range(columns):
            if p1[rows - 1][c] != p2[0][c]:
                return False
        return True
    elif dc == -1:  # left
        for r in range(rows):
            if p1[r][0] != p2[r][columns - 1]:
                return False
        return True
    else:
        assert False


def puzzle2(input_file) -> int:
    input_content = get_input_data(input_file)

    (tiles, tile_borders, rows, columns) = parse_input(input_content)

    corner_tile = -1
    adjacent_tiles = defaultdict(set)
    for tile_no1, borders1 in tile_borders.items():
        for tile_no2, borders2 in tile_borders.items():
            if tile_no1 == tile_no2:
                continue

            if borders1 & borders2:
                adjacent_tiles[tile_no1].add(tile_no2)

        if len(adjacent_tiles[tile_no1]) == 2:
            corner_tile = tile_no1

    img_rows = int(math.sqrt(len(tile_borders)))
    img_cols = int(math.sqrt(len(tile_borders)))
    img_tiles_used = set()
    assert len(tile_borders) == img_rows * img_cols
    img_tiles = [[None for _ in range(img_rows)] for _ in range(img_cols)]
    img_tiles[0][0] = corner_tile
    img_tiles[0][1], img_tiles[1][0] = adjacent_tiles[corner_tile]
    img_tiles_used.add(img_tiles[0][0])
    img_tiles_used.add(img_tiles[0][1])
    img_tiles_used.add(img_tiles[1][1])

    neighbor_offset = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while True:
        if len(img_tiles_used) == img_rows * img_cols:
            break
        for r in range(img_rows):
            for c in range(img_cols):
                if img_tiles[r][c] is not None:
                    continue
                opts = set([k for k in adjacent_tiles.keys() if k not in img_tiles_used])
                for dr, dc in neighbor_offset:
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < img_rows and 0 <= cc < img_cols and img_tiles[rr][cc]:
                        opts = opts & adjacent_tiles[img_tiles[rr][cc]]
                if len(opts) == 1:
                    chosen = list(opts)[0]
                    img_tiles[r][c] = chosen
                    assert chosen not in img_tiles_used
                    img_tiles_used.add(chosen)

    PIECES = [[None for _ in range(img_rows)] for _ in range(img_cols)]
    for r in range(img_rows):
        for c in range(img_cols):
            opts = poss(tiles[img_tiles[r][c]])  # 8 ways of positioning a tile
            for dr, dc in neighbor_offset:
                rr, cc = r + dr, c + dc
                if 0 <= rr < img_rows and 0 <= cc < img_cols:
                    ok_nbr = set()
                    opts_nbr = poss(tiles[img_tiles[rr][cc]])  # 8 ways of positioning a neighboring tile
                    for o1 in opts:
                        for o2 in opts_nbr:
                            if matches(rows, columns, o1, o2, dr, dc):
                                ok_nbr.add(o1)
                    opts = opts & ok_nbr
            # Assumes that every piece has only one orientation that can match its neighbors
            assert len(opts) == 1
            PIECES[r][c] = list(opts)[0]

    for r in range(img_rows):
        for c in range(img_cols):
            for dr, dc in neighbor_offset:
                rr, cc = r + dr, c + dc
                if 0 <= rr < img_rows and 0 <= cc < img_cols:
                    p1 = PIECES[r][c]
                    p2 = PIECES[rr][cc]
                    assert matches(rows, columns, p1, p2, dr, dc)

    IMAGE = [['?' for _ in range(img_cols * (columns - 2))] for _ in range(img_rows * (rows - 2))]
    for r in range(img_rows):
        for c in range(img_cols):
            T = PIECES[r][c]
            assert T in poss(tiles[img_tiles[r][c]])
            for rr in range(1, len(T) - 1):
                for cc in range(1, len(T[rr]) - 1):
                    IMAGE[r * (rows - 2) + (rr - 1)][c * (columns - 2) + (cc - 1)] = T[rr][cc]

    M = ['                  # ',
         '#    ##    ##    ###',
         ' #  #  #  #  #  #   ']
    MR = len(M)
    MC = len(M[0])
    for row in M:
        assert len(row) == MC

    IR = len(IMAGE)
    IC = len(IMAGE[0])
    assert len(IMAGE) == IR
    for row in IMAGE:
        assert len(row) == IC

    for IM in poss(IMAGE):
        assert len(IM) == IR
        assert len(IM[0]) == IC
        IS_M = [[False for _ in range(len(IM[0]))] for _ in range(len(IM))]
        has_monster = False
        for r in range(IR):
            for c in range(IC):
                is_monster = True
                for mr in range(MR):
                    for mc in range(MC):
                        if not (0 <= r + mr < IR and 0 <= c + mc < IC):
                            is_monster = False
                        else:
                            if M[mr][mc] == '#' and IM[r + mr][c + mc] != '#':
                                is_monster = False
                if is_monster:
                    has_monster = True
                    for mr in range(MR):
                        for mc in range(MC):
                            if M[mr][mc] == '#':
                                IS_M[r + mr][c + mc] = True
        # Assumes only one orientation has sea monsters
        if has_monster:
            ans = 0
            for r in range(IR):
                for c in range(IC):
                    if IM[r][c] == '#' and not IS_M[r][c]:
                        ans += 1
            return ans


if __name__ == '__main__':
    answer = puzzle1("../resources/y2020/day20/day20_1.txt")
    print(answer)

    answer = puzzle1("../resources/y2020/day20/day20_2.txt")
    print(answer)

    answer = puzzle2("../resources/y2020/day20/day20_1.txt")
    print(answer)

    answer = puzzle2("../resources/y2020/day20/day20_2.txt")
    print(answer)
