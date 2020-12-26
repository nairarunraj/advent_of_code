"""
--- Day 9: Encoding Error ---
"""

from y2020.file_utils import get_input_data_as_int


def check_valid_input(input_content, window_start, window_end):
    if window_end == len(input_content):
        return None

    possible_candidates = []
    no_to_check = input_content[window_end]
    for i in range(window_start, window_end):
        if no_to_check < input_content[i]:
            continue

        possible_candidates.append(input_content[i])

    possible_candidates.sort()

    left_index = 0
    right_index = len(possible_candidates) - 1
    while left_index <= right_index:
        if possible_candidates[left_index] + possible_candidates[right_index] == no_to_check:
            return check_valid_input(input_content, window_start + 1, window_end + 1)

        if possible_candidates[left_index] + possible_candidates[right_index] < no_to_check:
            left_index += 1

        if possible_candidates[left_index] + possible_candidates[right_index] > no_to_check:
            right_index -= 1

    return no_to_check


def puzzle1(input_file, preamble_length) -> int:
    input_content = get_input_data_as_int(input_file)

    return check_valid_input(input_content, 0, preamble_length)


def puzzle2(input_file, preamble_length) -> int:
    input_content = get_input_data_as_int(input_file)

    invalid_no = puzzle1(input_file, preamble_length)

    current_sum = 0
    window_start = 0
    window_end = -1
    while True:
        if current_sum == invalid_no:
            sum_list = input_content[window_start: window_end + 1]
            min_no = min(sum_list)
            max_no = max(sum_list)
            return min_no + max_no

        if current_sum < invalid_no:
            window_end += 1
            current_sum += input_content[window_end]
        elif current_sum > invalid_no:
            current_sum -= input_content[window_start]
            window_start += 1


if __name__ == '__main__':
    answer = puzzle1("../../resources/y2020/day9/day9_1.txt", 5)
    print(answer)

    answer = puzzle1("../../resources/y2020/day9/day9_2.txt", 25)
    print(answer)

    answer = puzzle2("../../resources/y2020/day9/day9_1.txt", 5)
    print(answer)

    answer = puzzle2("../../resources/y2020/day9/day9_2.txt", 25)
    print(answer)
