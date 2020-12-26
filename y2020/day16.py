"""
--- Day 16: Ticket Translation ---
"""

from y2020.file_utils import get_input_data


def puzzle1(input_file) -> int:
    input_content = get_input_data(input_file)

    ticket_rules = {}
    your = False
    nearby = False
    nearby_tickets = []
    for line in input_content:
        if line == '': continue

        if line == 'your ticket:':
            your = True
            continue

        if line == 'nearby tickets:':
            nearby = True
            continue

        if not your and not nearby:
            rule = line.split(":")
            ranges = rule[1].lstrip().split(' or ')
            ticket_rules[rule[0]] = [[int(limit) for limit in vals.split('-')] for vals in ranges]
            continue

        if nearby:
            nearby_tickets.append([int(ticket) for ticket in line.split(',')])

    invalid_tickets = []
    for ticket_row in nearby_tickets:
        for ticket in ticket_row:
            valid_ticket = False
            for rules in ticket_rules.values():
                if rules[0][0] <= ticket <= rules[0][1] or rules[1][0] <= ticket <= rules[1][1]:
                    valid_ticket = True
                    break
            if not valid_ticket:
                invalid_tickets.append(ticket)

    return sum(invalid_tickets)


def get_row_index(no_of_rules, final_cols, ticket_rules, valid_tickets):
    if len(final_cols) == no_of_rules:
        return final_cols

    rule_col = {}
    for index in range(no_of_rules):
        if index in final_cols: continue

        for rname, rule in ticket_rules.items():
            invalid_col = False
            for ticket_row in valid_tickets:
                ticket = ticket_row[index]
                if ticket < rule[0][0] or rule[0][1] < ticket < rule[1][0] or rule[1][1] < ticket:
                    invalid_col = True

            if not invalid_col:
                if rname not in rule_col: rule_col[rname] = []

                rule_col[rname].append(index)

    for name, indexes in rule_col.items():
        if len(indexes) == 1: final_cols[indexes[0]] = name

    return get_row_index(no_of_rules, final_cols, ticket_rules, valid_tickets)


def puzzle2(input_file) -> int:
    input_content = get_input_data(input_file)

    ticket_rules = {}
    your = False
    nearby = False
    your_tickets = []
    nearby_tickets = []
    for line in input_content:
        if line == '': continue

        if line == 'your ticket:':
            your = True
            continue

        if line == 'nearby tickets:':
            nearby = True
            continue

        if not your and not nearby:
            rule = line.split(":")
            ranges = rule[1].lstrip().split(' or ')
            ticket_rules[rule[0]] = [[int(limit) for limit in vals.split('-')] for vals in ranges]
            continue

        if your and not nearby:
            your_tickets = [int(ticket) for ticket in line.split(',')]
            continue

        if nearby:
            nearby_tickets.append([int(ticket) for ticket in line.split(',')])

    valid_tickets = []
    for ticket_row in nearby_tickets:
        valid_ticket_row = True
        for ticket in ticket_row:
            valid_ticket = False
            for rules in ticket_rules.values():
                if rules[0][0] <= ticket <= rules[0][1] or rules[1][0] <= ticket <= rules[1][1]:
                    valid_ticket = True
            if not valid_ticket:
                valid_ticket_row = False
                break

        if valid_ticket_row:
            valid_tickets.append(ticket_row)

    no_of_rules = len(your_tickets)
    final_cols = get_row_index(no_of_rules, {}, ticket_rules, valid_tickets)

    product = 1
    for index, name in final_cols.items():
        if name.startswith('departure '):
            product *= your_tickets[index]

    return product


if __name__ == '__main__':
    answer = puzzle1("../resources/y2020/day16/day16_1.txt")
    print(answer)

    answer = puzzle1("../resources/y2020/day16/day16_2.txt")
    print(answer)

    answer = puzzle2("../resources/y2020/day16/day16_1.txt")
    print(answer)

    answer = puzzle2("../resources/y2020/day16/day16_3.txt")
    print(answer)

    answer = puzzle2("../resources/y2020/day16/day16_2.txt")
    print(answer)
