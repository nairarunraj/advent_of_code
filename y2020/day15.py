"""
--- Day 15: Rambunctious Recitation ---
"""

from y2020.file_utils import get_csv_input_data_as_int


def puzzle1(input_file, max_turn) -> int:
    input_content = get_csv_input_data_as_int(input_file)

    visited = {no: idx for idx, no in enumerate(input_content, 1)}

    prev_no = 0

    for current_turn in range(len(input_content) + 1, max_turn):
        if prev_no not in visited:
            visited[prev_no] = current_turn
            prev_no = 0
        else:
            next_no = current_turn - visited[prev_no]
            visited[prev_no] = current_turn
            prev_no = next_no

    return prev_no


def puzzle2(input_file, max_turns) -> int:
    return puzzle1(input_file, max_turns)


if __name__ == '__main__':
    answer = puzzle1("../../resources/y2020/day15/day15_1.txt", 2020)
    print(answer)

    answer = puzzle1("../../resources/y2020/day15/day15_2.txt", 2020)
    print(answer)

    answer = puzzle2("../../resources/y2020/day15/day15_1.txt", 30000000)
    print(answer)

    answer = puzzle2("../../resources/y2020/day15/day15_2.txt", 30000000)
    print(answer)
