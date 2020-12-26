"""
--- Day 3: Toboggan Trajectory ---
"""

from y2020.file_utils import get_input_data


def get_tree_count_for_slope(input_content, slope_x, slope_y):
    max_len = len(input_content)
    start_row = start_col = tree_count = 0

    while start_row < max_len:
        line = input_content[start_row]
        col_len = len(line)
        if start_col >= col_len:
            start_col = start_col % col_len
        if line[start_col] == '#':
            tree_count += 1

        start_col += slope_x
        start_row += slope_y

    return tree_count


def puzzle1(input_file) -> int:
    input_content = get_input_data(input_file)

    return get_tree_count_for_slope(input_content, 3, 1)


def puzzle2(input_file) -> int:
    slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))

    input_content = get_input_data(input_file)

    product = 1
    for (slope_x, slope_y) in slopes:
        product *= get_tree_count_for_slope(input_content, slope_x, slope_y)

    return product


if __name__ == '__main__':
    answer = puzzle1("../../resources/y2020/day3/day3_1.txt")
    print(answer)

    answer = puzzle1("../../resources/y2020/day3/day3_2.txt")
    print(answer)

    answer = puzzle2("../../resources/y2020/day3/day3_1.txt")
    print(answer)

    answer = puzzle2("../../resources/y2020/day3/day3_2.txt")
    print(answer)
