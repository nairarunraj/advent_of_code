"""
--- Day 11: Seating System ---
"""

from y2020.file_utils import get_input_data


def get_occupied_seats(seating_arr):
    occupied_seats = 0
    for row in seating_arr:
        for seat in row:
            if seat == '#': occupied_seats += 1

    return occupied_seats


def apply_rules(seating_arr, row_len, col_len):
    new_seating = [['.' for _ in range(col_len)] for _ in range(row_len)]
    for row in range(row_len):
        for col in range(col_len):
            occupied_adjacent_seats = 0
            current_seat = seating_arr[row][col]

            # West
            if col - 1 >= 0 and seating_arr[row][col - 1] == '#':
                occupied_adjacent_seats += 1

            # East
            if col + 1 < col_len and seating_arr[row][col + 1] == '#':
                occupied_adjacent_seats += 1

            # South
            if row + 1 < row_len and seating_arr[row + 1][col] == '#':
                occupied_adjacent_seats += 1

            # North
            if row - 1 >= 0 and seating_arr[row - 1][col] == '#':
                occupied_adjacent_seats += 1

            # North-West
            if col - 1 >= 0 and row - 1 >= 0 and seating_arr[row - 1][col - 1] == '#':
                occupied_adjacent_seats += 1

            # South-West
            if col - 1 >= 0 and row + 1 < row_len and seating_arr[row + 1][col - 1] == '#':
                occupied_adjacent_seats += 1

            # North-East
            if col + 1 < col_len and row - 1 >= 0 and seating_arr[row - 1][col + 1] == '#':
                occupied_adjacent_seats += 1

            # South-East
            if col + 1 < col_len and row + 1 < row_len and seating_arr[row + 1][col + 1] == '#':
                occupied_adjacent_seats += 1

            if current_seat == 'L' and occupied_adjacent_seats == 0:
                new_seating[row][col] = '#'
            elif current_seat == '#' and occupied_adjacent_seats >= 4:
                new_seating[row][col] = 'L'
            else:
                new_seating[row][col] = current_seat

    if new_seating != seating_arr:
        return apply_rules(new_seating, row_len, col_len)

    return get_occupied_seats(new_seating)


def puzzle1(input_file) -> int:
    input_content = get_input_data(input_file)

    row_len = len(input_content)
    col_len = len(input_content[0])
    return apply_rules(input_content, row_len, col_len)


def is_west_seat_occupied(seating_arr, row, col, row_len, col_len, occupied_seat_map, key):
    if key in occupied_seat_map:
        return occupied_seat_map[key]

    if col - 1 < 0:
        return False

    if seating_arr[row][col - 1] == 'L':
        return False

    if seating_arr[row][col - 1] == '#':
        return True

    next_key = str(row) + ":" + str(col - 1) + ":W"
    is_seat_occupied = is_west_seat_occupied(seating_arr, row, col - 1, row_len, col_len, occupied_seat_map, next_key)
    occupied_seat_map[key] = is_seat_occupied
    return is_seat_occupied


def is_east_seat_occupied(seating_arr, row, col, row_len, col_len, occupied_seat_map, key):
    if key in occupied_seat_map:
        return occupied_seat_map[key]

    if col + 1 == col_len:
        return False

    if seating_arr[row][col + 1] == 'L':
        return False

    if seating_arr[row][col + 1] == '#':
        return True

    next_key = str(row) + ":" + str(col + 1) + ":E"
    is_seat_occupied = is_east_seat_occupied(seating_arr, row, col + 1, row_len, col_len, occupied_seat_map, next_key)
    occupied_seat_map[key] = is_seat_occupied
    return is_seat_occupied


def is_north_seat_occupied(seating_arr, row, col, row_len, col_len, occupied_seat_map, key):
    if key in occupied_seat_map:
        return occupied_seat_map[key]

    if row - 1 < 0:
        return False

    if seating_arr[row - 1][col] == 'L':
        return False

    if seating_arr[row - 1][col] == '#':
        return True

    next_key = str(row - 1) + ":" + str(col) + ":N"
    is_seat_occupied = is_north_seat_occupied(seating_arr, row - 1, col, row_len, col_len, occupied_seat_map, next_key)
    occupied_seat_map[key] = is_seat_occupied
    return is_seat_occupied


def is_ne_seat_occupied(seating_arr, row, col, row_len, col_len, occupied_seat_map, key):
    if key in occupied_seat_map:
        return occupied_seat_map[key]

    if col + 1 == col_len:
        return False

    if row - 1 < 0:
        return False

    if seating_arr[row - 1][col + 1] == 'L':
        return False

    if seating_arr[row - 1][col + 1] == '#':
        return True

    next_key = str(row - 1) + ":" + str(col + 1) + ":NE"
    is_seat_occupied = is_ne_seat_occupied(seating_arr, row - 1, col + 1, row_len, col_len, occupied_seat_map, next_key)
    occupied_seat_map[key] = is_seat_occupied
    return is_seat_occupied


def is_nw_seat_occupied(seating_arr, row, col, row_len, col_len, occupied_seat_map, key):
    if key in occupied_seat_map:
        return occupied_seat_map[key]

    if col - 1 < 0:
        return False

    if row - 1 < 0:
        return False

    if seating_arr[row - 1][col - 1] == 'L':
        return False

    if seating_arr[row - 1][col - 1] == '#':
        return True

    next_key = str(row - 1) + ":" + str(col - 1) + ":NW"
    is_seat_occupied = is_nw_seat_occupied(seating_arr, row - 1, col - 1, row_len, col_len, occupied_seat_map, next_key)
    occupied_seat_map[key] = is_seat_occupied
    return is_seat_occupied


def is_south_seat_occupied(seating_arr, row, col, row_len, col_len, occupied_seat_map, key):
    if key in occupied_seat_map:
        return occupied_seat_map[key]

    if row + 1 == row_len:
        return False

    if seating_arr[row + 1][col] == 'L':
        return False

    if seating_arr[row + 1][col] == '#':
        return True

    next_key = str(row + 1) + ":" + str(col) + ":S"
    is_seat_occupied = is_south_seat_occupied(seating_arr, row + 1, col, row_len, col_len, occupied_seat_map, next_key)
    occupied_seat_map[key] = is_seat_occupied
    return is_seat_occupied


def is_se_seat_occupied(seating_arr, row, col, row_len, col_len, occupied_seat_map, key):
    if key in occupied_seat_map:
        return occupied_seat_map[key]

    if row + 1 == row_len:
        return False

    if col + 1 == col_len:
        return False

    if seating_arr[row + 1][col + 1] == 'L':
        return False

    if seating_arr[row + 1][col + 1] == '#':
        return True

    next_key = str(row + 1) + ":" + str(col + 1) + ":SE"
    is_seat_occupied = is_se_seat_occupied(seating_arr, row + 1, col + 1, row_len, col_len, occupied_seat_map, next_key)
    occupied_seat_map[key] = is_seat_occupied
    return is_seat_occupied


def is_sw_seat_occupied(seating_arr, row, col, row_len, col_len, occupied_seat_map, key):
    if key in occupied_seat_map:
        return occupied_seat_map[key]

    if row + 1 == row_len:
        return False

    if col - 1 < 0:
        return False

    if seating_arr[row + 1][col - 1] == 'L':
        return False

    if seating_arr[row + 1][col - 1] == '#':
        return True

    next_key = str(row + 1) + ":" + str(col - 1) + ":SW"
    is_seat_occupied = is_sw_seat_occupied(seating_arr, row + 1, col - 1, row_len, col_len, occupied_seat_map, next_key)
    occupied_seat_map[key] = is_seat_occupied
    return is_seat_occupied


def apply_rules2(seating_arr, row_len, col_len):
    new_seating = [['.' for _ in range(col_len)] for _ in range(row_len)]
    occupied_seat_map = {}
    for row in range(0, row_len):
        for col in range(0, col_len):
            occupied_adjacent_seats = 0
            current_seat = seating_arr[row][col]

            pos_index = str(row) + ":" + str(col)

            # West
            if is_west_seat_occupied(seating_arr, row, col, row_len, col_len, occupied_seat_map, pos_index + ":W"):
                occupied_seat_map[pos_index + ":W"] = True
                occupied_adjacent_seats += 1
            else:
                occupied_seat_map[pos_index + ":W"] = False

            # East
            if is_east_seat_occupied(seating_arr, row, col, row_len, col_len, occupied_seat_map, pos_index + ":E"):
                occupied_seat_map[pos_index + ":E"] = True
                occupied_adjacent_seats += 1
            else:
                occupied_seat_map[pos_index + ":E"] = False

            # South
            if is_south_seat_occupied(seating_arr, row, col, row_len, col_len, occupied_seat_map, pos_index + ":S"):
                occupied_seat_map[pos_index + ":S"] = True
                occupied_adjacent_seats += 1
            else:
                occupied_seat_map[pos_index + ":S"] = False

            # North
            if is_north_seat_occupied(seating_arr, row, col, row_len, col_len, occupied_seat_map, pos_index + ":N"):
                occupied_seat_map[pos_index + ":N"] = True
                occupied_adjacent_seats += 1
            else:
                occupied_seat_map[pos_index + ":N"] = False

            # North-West
            if is_nw_seat_occupied(seating_arr, row, col, row_len, col_len, occupied_seat_map, pos_index + ":NW"):
                occupied_seat_map[pos_index + ":NW"] = True
                occupied_adjacent_seats += 1
            else:
                occupied_seat_map[pos_index + ":NW"] = False

            # South-West
            if is_sw_seat_occupied(seating_arr, row, col, row_len, col_len, occupied_seat_map, pos_index + ":SW"):
                occupied_seat_map[pos_index + ":SW"] = True
                occupied_adjacent_seats += 1
            else:
                occupied_seat_map[pos_index + ":SW"] = False

            # North-East
            if is_ne_seat_occupied(seating_arr, row, col, row_len, col_len, occupied_seat_map, pos_index + ":NE"):
                occupied_seat_map[pos_index + ":NE"] = True
                occupied_adjacent_seats += 1
            else:
                occupied_seat_map[pos_index + ":NE"] = False

            # South-East
            if is_se_seat_occupied(seating_arr, row, col, row_len, col_len, occupied_seat_map, pos_index + ":SE"):
                occupied_seat_map[pos_index + ":SE"] = True
                occupied_adjacent_seats += 1
            else:
                occupied_seat_map[pos_index + ":SE"] = False

            if current_seat == 'L' and occupied_adjacent_seats == 0:
                new_seating[row][col] = '#'
            elif current_seat == '#' and occupied_adjacent_seats >= 5:
                new_seating[row][col] = 'L'
            else:
                new_seating[row][col] = current_seat

    if new_seating != seating_arr:
        return apply_rules2(new_seating, row_len, col_len)

    return get_occupied_seats(new_seating)


def puzzle2(input_file) -> int:
    input_content = get_input_data(input_file)

    row_len = len(input_content)
    col_len = len(input_content[0])
    return apply_rules2(input_content, row_len, col_len)


if __name__ == '__main__':
    answer = puzzle1("../../resources/y2020/day11/day11_1.txt")
    print(answer)

    answer = puzzle1("../../resources/y2020/day11/day11_2.txt")
    print(answer)

    answer = puzzle2("../../resources/y2020/day11/day11_1.txt")
    print(answer)

    answer = puzzle2("../../resources/y2020/day11/day11_2.txt")
    print(answer)
