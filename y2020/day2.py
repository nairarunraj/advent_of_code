"""
--- Day 2: Password Philosophy ---
"""

from y2020.file_utils import get_input_data


def puzzle1(input_file) -> int:
    input_content = get_input_data(input_file)
    valid_passwords = 0
    for policy in input_content:
        (char_restriction, character, password) = policy.split(" ")
        character = character.rstrip(":")

        char_count = 0
        for pass_char in password:
            if pass_char == character:
                char_count += 1

        (min_chars, max_chars) = [int(number) for number in char_restriction.split('-')]

        if min_chars <= char_count <= max_chars:
            valid_passwords += 1

    return valid_passwords


def puzzle2(input_file) -> int:
    input_content = get_input_data(input_file)
    valid_passwords = 0
    for policy in input_content:
        (char_restriction, character, password) = policy.split(" ")
        character = character.rstrip(":")

        (first_index, second_index) = [int(number) - 1 for number in char_restriction.split('-')]

        if bool(password[first_index] == character) != bool(password[second_index] == character):
            valid_passwords += 1

    return valid_passwords


if __name__ == '__main__':
    answer = puzzle1("../../resources/y2020/day2/day2_1.txt")
    print(answer)

    answer = puzzle1("../../resources/y2020/day2/day2_2.txt")
    print(answer)

    answer = puzzle2("../../resources/y2020/day2/day2_1.txt")
    print(answer)

    answer = puzzle2("../../resources/y2020/day2/day2_2.txt")
    print(answer)
