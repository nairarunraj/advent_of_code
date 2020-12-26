"""
--- Day 5: Binary Boarding ---
"""

from y2020.file_utils import get_input_data


def get_row(row_code, current_char_index, start_row, end_row):
    if end_row - start_row == 1:
        if row_code[current_char_index] == 'B':
            return end_row

        return start_row

    if row_code[current_char_index] == 'B':
        return get_row(row_code, current_char_index + 1, int((start_row + end_row) / 2) + 1, end_row)

    return get_row(row_code, current_char_index + 1, start_row, int((start_row + end_row) / 2))


def get_col(col_code, current_char_index, start_col, end_col):
    if end_col - start_col == 1:
        if col_code[current_char_index] == 'R':
            return end_col

        return start_col

    if col_code[current_char_index] == 'R':
        return get_col(col_code, current_char_index + 1, int((start_col + end_col) / 2) + 1, end_col)

    return get_col(col_code, current_char_index + 1, start_col, int((start_col + end_col) / 2))


def get_seat_id(seat_code):
    row_code = seat_code[:7]
    start_row = 0
    end_row = 127
    current_char_index = 0
    row_no = get_row(row_code, current_char_index, start_row, end_row)

    col_code = seat_code[7:]
    start_col = 0
    end_col = 7
    current_char_index = 0
    col_no = get_col(col_code, current_char_index, start_col, end_col)

    return row_no * 8 + col_no


def puzzle1(input_file) -> int:
    input_content = get_input_data(input_file)

    max_seat_id = 0

    for seat_code in input_content:
        seat_id = get_seat_id(seat_code)
        if seat_id > max_seat_id: max_seat_id = seat_id

    return max_seat_id


def puzzle2(input_file) -> int:
    input_content = get_input_data(input_file)

    seat_map = [0 for _ in range(1024)]

    for seat_code in input_content:
        seat_id = get_seat_id(seat_code)
        seat_map[seat_id] = 1

    first_occupant_found = False
    for seat_id in range(1024):
        if first_occupant_found and seat_map[seat_id] == 0:
            return seat_id

        if seat_map[seat_id] == 1:
            first_occupant_found = True

    return 0


if __name__ == '__main__':
    answer = puzzle1("../../resources/y2020/day5/day5_1.txt")
    print(answer)

    answer = puzzle1("../../resources/y2020/day5/day5_2.txt")
    print(answer)

    answer = puzzle2("../../resources/y2020/day5/day5_2.txt")
    print(answer)
