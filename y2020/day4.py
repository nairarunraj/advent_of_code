"""
--- Day 4: Passport Processing ---
"""

from y2020.file_utils import get_input_data_newline_separated


def puzzle1(input_file) -> int:
    input_content = get_input_data_newline_separated(input_file)
    valid_passport = 0
    for passport_info in input_content:
        cid_present = False
        total_fields = 0
        for line in passport_info:
            if line.find("cid:") != -1:
                cid_present = True

            total_fields += len(line.split(' '))

        if total_fields == 8:
            valid_passport += 1
        elif total_fields == 7 and not cid_present:
            valid_passport += 1

    return valid_passport


def four_digits(year):
    if len(year) != 4:
        return False

    return True


def valid_yr_range(year, min_yr, max_yr):
    if not year.isnumeric():
        return False

    int_yr = int(year)

    if min_yr > int_yr or int_yr > max_yr:
        return False

    return True


def byr_check(birth_year):
    if not four_digits(birth_year):
        return False

    if not valid_yr_range(birth_year, 1920, 2002):
        return False

    return True


def iyr_check(issue_year):
    if not four_digits(issue_year):
        return False

    if not valid_yr_range(issue_year, 2010, 2020):
        return False

    return True


def eyr_check(exp_year):
    if not four_digits(exp_year):
        return False

    if not valid_yr_range(exp_year, 2020, 2030):
        return False

    return True


def height_check(height_val, min_height, max_height):
    if not height_val.isnumeric():
        return False

    int_height_val = int(height_val)

    if int_height_val < min_height or int_height_val > max_height:
        return False

    return True


def hgt_check(height):
    unit = height[-2:]

    if unit not in ('cm', 'in'):
        return False

    height_val = height[:-2]

    if unit == 'cm':
        return height_check(height_val, 150, 193)

    if unit == 'in':
        return height_check(height_val, 59, 76)


def hcl_check(hair_color):
    if hair_color[0] != '#' or len(hair_color) != 7:
        return False

    valid_chars = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'}

    for char in hair_color[1:]:
        if char not in valid_chars:
            return False

    return True


def ecl_check(eye_color):
    if eye_color not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        return False

    return True


def pid_check(pid):
    if len(pid) != 9:
        return False

    try:
        int_pid = int(pid)
    except:
        return False

    return True


def is_data_valid(passport_info):
    for line in passport_info:
        fields = line.split(' ')
        for field in fields:
            (key, val) = field.split(':')

            if key == 'byr' and not byr_check(val):
                return False
            if key == 'iyr' and not iyr_check(val):
                return False
            if key == 'eyr' and not eyr_check(val):
                return False
            if key == 'hgt' and not hgt_check(val):
                return False
            if key == 'hcl' and not hcl_check(val):
                return False
            if key == 'ecl' and not ecl_check(val):
                return False
            if key == 'pid' and not pid_check(val):
                return False

    return True


def puzzle2(input_file) -> int:
    input_content = get_input_data_newline_separated(input_file)
    valid_passport = 0
    for passport_info in input_content:
        cid_present = False
        total_fields = 0
        for line in passport_info:
            if line.find("cid:") != -1:
                cid_present = True

            total_fields += len(line.split(' '))

        if (total_fields == 8 or (total_fields == 7 and not cid_present)) and is_data_valid(passport_info):
            valid_passport += 1

    return valid_passport


if __name__ == '__main__':
    answer = puzzle1("../../resources/y2020/day4/day4_1.txt")
    print(answer)

    answer = puzzle1("../../resources/y2020/day4/day4_2.txt")
    print(answer)

    answer = puzzle2("../../resources/y2020/day4/day4_1.txt")
    print(answer)

    answer = puzzle2("../../resources/y2020/day4/day4_2.txt")
    print(answer)
