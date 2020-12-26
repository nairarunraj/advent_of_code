"""
--- Day 10: Adapter Array ---
"""

from functools import lru_cache

from y2020.file_utils import get_input_data_as_int


def puzzle1(input_file) -> int:
    input_content = get_input_data_as_int(input_file)

    joltage = sorted(input_content)
    joltage.append(joltage[-1] + 3)
    joltage.insert(0, 0)
    if joltage[0] > 3:
        return None

    current_index = 1

    difference_arr = [0 for _ in range(4)]

    while current_index < len(joltage):
        difference = joltage[current_index] - joltage[current_index - 1]
        if difference > 3 or difference_arr == 0:
            return None

        difference_arr[difference] += 1
        current_index += 1

    return difference_arr[1] * difference_arr[3]


@lru_cache(maxsize=None)
def distinct_arrangements(joltage, current_index):
    next_index = current_index + 1

    if next_index == len(joltage):
        return 1

    path_count = 0
    while joltage[next_index] - joltage[current_index] < 4:
        nested_path_count = distinct_arrangements(joltage, next_index)
        path_count += nested_path_count
        next_index += 1
        if next_index == len(joltage):
            break

    return path_count


def puzzle2(input_file) -> int:
    input_content = get_input_data_as_int(input_file)

    joltage_list = sorted(input_content)
    joltage_list.append(joltage_list[-1] + 3)
    joltage_list.insert(0, 0)

    joltage = tuple(joltage_list)
    return distinct_arrangements(joltage, 0)


if __name__ == '__main__':
    answer = puzzle1("../../resources/y2020/day10/day10_1.txt")
    print(answer)

    answer = puzzle1("../../resources/y2020/day10/day10_2.txt")
    print(answer)

    answer = puzzle2("../../resources/y2020/day10/day10_1.txt")
    print(answer)

    answer = puzzle2("../../resources/y2020/day10/day10_3.txt")
    print(answer)

    answer = puzzle2("../../resources/y2020/day10/day10_2.txt")
    print(answer)
