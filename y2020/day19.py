"""
--- Day 19: Monster Messages ---
"""

from y2020.file_utils import get_input_data


def parse_input(input_content):
    rules = {}
    all_rules_processed = False

    strings_to_check = []
    for line in input_content:
        if line == '':
            all_rules_processed = True
            continue

        if not all_rules_processed:
            (rule_no, rule) = line.split(': ')
            if rule[0] == '"':
                rules[rule_no] = [[rule]]
                continue

            options = rule.split(' | ')
            rules[rule_no] = []
            for option in options:
                rules[rule_no].append(option.split(' '))
            continue

        strings_to_check.append(line)

    return rules, strings_to_check


def puzzle1(input_file) -> int:
    input_content = get_input_data(input_file)

    (rules, strings_to_check) = parse_input(input_content)

    valid_strings = 0
    for line in strings_to_check:
        if len(line) in is_line_valid(rules, '0', line, 0):
            valid_strings += 1

    return valid_strings


def is_line_valid(rules, idx, sample, start):
    rule = rules[idx]
    if rule[0][0][0] == '"':
        # terminal rule must match
        # if it doesn't return an empty set signifying invalid string
        return {start + 1} if start < len(sample) and rule[0][0][1] == sample[start] else set()
    else:
        # non-terminal (sub-rules)
        endings = set()
        for sub_rule in rule:
            buffer = {start}
            for part in sub_rule:
                temp = set()
                for loc in buffer:
                    temp = temp | is_line_valid(rules, part, sample, loc)
                buffer = temp
            endings = endings | buffer
        return endings


def puzzle2(input_file) -> int:
    input_content = get_input_data(input_file)

    (rules, strings_to_check) = parse_input(input_content)

    rules['8'] = [['42'], ['42', '8']]
    rules['11'] = [['42', '31'], ['42', '11', '31']]

    valid_strings = 0
    for line in strings_to_check:
        if len(line) in is_line_valid(rules, '0', line, 0):
            valid_strings += 1

    return valid_strings


if __name__ == '__main__':
    answer = puzzle1("../resources/y2020/day19/day19_1.txt")
    print(answer)

    answer = puzzle1("../resources/y2020/day19/day19_2.txt")
    print(answer)

    answer = puzzle2("../resources/y2020/day19/day19_1.txt")
    print(answer)

    answer = puzzle2("../resources/y2020/day19/day19_3.txt")
    print(answer)

    answer = puzzle2("../resources/y2020/day19/day19_2.txt")
    print(answer)
