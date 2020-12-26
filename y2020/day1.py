"""
--- Day 1: Report Repair ---
"""

from y2020.file_utils import get_input_data_as_int


def puzzle1(input_file) -> int:
    input_content = get_input_data_as_int(input_file)
    sorted_arr = sorted(input_content)

    i = 0
    j = len(sorted_arr) - 1
    while i < j:
        sum_nos = sorted_arr[i] + sorted_arr[j]

        if sum_nos == 2020:
            return sorted_arr[i] * sorted_arr[j]

        if sum_nos < 2020:
            i += 1
        else:
            j -= 1

    return 0


def puzzle2_find_ans(sorted_arr: list, visited: dict, i: int, j: int) -> int:
    k = int((i + j) / 2)
    while i < k < j:
        visited_key = (i, k, j)
        if visited_key in visited: break

        sum_nos = sorted_arr[i] + sorted_arr[j] + sorted_arr[k]

        if sum_nos == 2020:
            return sorted_arr[i] * sorted_arr[j] * sorted_arr[k]

        visited[visited_key] = 1

        if sum_nos < 2020:
            k += 1
        else:
            k -= 1

    return 0


def puzzle2_recursion(sorted_arr, visited, i, j) -> int:
    while i < j:
        if (product_ans := puzzle2_find_ans(sorted_arr, visited, i, j)) != 0:
            return product_ans

        if sorted_arr[i] + sorted_arr[j - 1] + sorted_arr[j] < 2020:
            # sum of the two highest elements with the lowest element falls short
            # move to the next lowest element
            i += 1
        elif sorted_arr[i] + sorted_arr[i + 1] + sorted_arr[j] > 2020:
            # sum of the two lowest elements with the highest element is still higher
            # move to the next highest element
            j -= 1
        else:
            # Repeat the process for 2 scenarios-
            # 1. Increment the lower counter
            # 2. Decrement the higher counter
            return puzzle2_recursion(sorted_arr, visited, i + 1, j) or puzzle2_recursion(sorted_arr, visited, i, j - 1)

    return 0


def puzzle2(input_file):
    input_content = get_input_data_as_int(input_file)
    sorted_arr = sorted(input_content)

    i = 0
    j = len(sorted_arr) - 1
    visited = {}

    return puzzle2_recursion(sorted_arr, visited, i, j)


if __name__ == '__main__':
    answer = puzzle1("../../resources/y2020/day1/day1_2.txt")
    print(answer)

    answer = puzzle2("../../resources/y2020/day1/day1_2.txt")
    print(answer)
