"""
--- Day 6: Custom Customs ---
"""

from y2020.file_utils import get_input_data


def get_rules(input_content):
    color_rules = {}
    bag_contain_rules = {}
    for rule in input_content:
        rule = rule.replace("bags", "")
        rule = rule.replace("bag", "")
        rule = rule.rstrip(".")
        (bag_info, contains_info) = rule.split(' contain ')
        bag_info = bag_info.rstrip(" ")
        if contains_info.find('no other') != -1:
            color_rules[bag_info] = []
            continue

        multiple_contains = contains_info.split(",")
        for color_contains in multiple_contains:
            color_contains = color_contains.rstrip(' ')
            color_contains = color_contains.lstrip(' ')
            (no, color) = color_contains.split(' ', 1)
            if bag_info in color_rules:
                color_rules[bag_info].append((color, int(no)))
            else:
                color_rules[bag_info] = [(color, int(no))]

            if color not in bag_contain_rules:
                bag_contain_rules[color] = dict()

            bag_contain_rules[color][bag_info] = no

    return (color_rules, bag_contain_rules)


def puzzle1(input_file) -> int:
    input_content = get_input_data(input_file)
    color_rules, bag_contain_rules = get_rules(input_content)

    shiny_gold_bags = []
    visited = {}
    for bag in bag_contain_rules['shiny gold'].keys():
        visited[bag] = 1
        shiny_gold_bags.append(bag)

    current_index = 0
    while True:
        if current_index == len(shiny_gold_bags):
            break

        current_color = shiny_gold_bags[current_index]
        if current_color not in bag_contain_rules:
            current_index += 1
            continue

        for bag in bag_contain_rules[current_color].keys():

            if bag == 'shiny gold':
                current_index += 1
                continue
            if bag not in visited:
                shiny_gold_bags.append(bag)
                visited[bag] = 1

        current_index += 1

    return len(shiny_gold_bags)


def get_internal_bags(color_rules, bag_color):
    bag_count = 0
    for bag_content in color_rules[bag_color]:
        bag_count += bag_content[1]
        bag_count += (bag_content[1] * get_internal_bags(color_rules, bag_content[0]))

    return bag_count


def puzzle2(input_file) -> int:
    input_content = get_input_data(input_file)

    color_rules, bag_contain_rules = get_rules(input_content)

    total_count = get_internal_bags(color_rules, 'shiny gold')

    return total_count


if __name__ == '__main__':
    answer = puzzle1("../../resources/y2020/day7/day7_1.txt")
    print(answer)

    answer = puzzle1("../../resources/y2020/day7/day7_2.txt")
    print(answer)

    answer = puzzle2("../../resources/y2020/day7/day7_1.txt")
    print(answer)

    answer = puzzle2("../../resources/y2020/day7/day7_2.txt")
    print(answer)
