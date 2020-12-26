"""
--- Day 23: Crab Cups ---
"""

from y2020.file_utils import get_input_line


def solve(input_line, is_puzzle2):
    no_of_cups = len(input_line) if (not is_puzzle2) else int(1e6)
    next_cup = [None for _ in range(no_of_cups + 1)]
    cup_labels = [int(cup_label) for cup_label in input_line]

    for i in range(len(cup_labels)):
        next_cup[cup_labels[i]] = cup_labels[(i + 1) % len(cup_labels)]

    if is_puzzle2:
        next_cup[cup_labels[-1]] = len(cup_labels) + 1
        for i in range(len(cup_labels) + 1, no_of_cups + 1):
            next_cup[i] = i + 1
        next_cup[-1] = cup_labels[0]

    t = 0
    current = cup_labels[0]
    nmoves = int(1e7) if is_puzzle2 else 100
    for _ in range(nmoves):
        t += 1
        pickup = next_cup[current]
        next_cup[current] = next_cup[next_cup[next_cup[pickup]]]

        dest = no_of_cups if current == 1 else current - 1
        while dest in [pickup, next_cup[pickup], next_cup[next_cup[pickup]]]:
            dest = no_of_cups if dest == 1 else dest - 1

        next_cup[next_cup[next_cup[pickup]]] = next_cup[dest]
        next_cup[dest] = pickup
        current = next_cup[current]

    if is_puzzle2:
        return next_cup[1] * next_cup[next_cup[1]]
    else:
        ans = []
        x = next_cup[1]
        while x != 1:
            ans.append(x)
            x = next_cup[x]
        return ''.join([str(x) for x in ans])


def puzzle1(input_file) -> str:
    input_line = get_input_line(input_file)

    return solve(input_line, False)


def puzzle2(input_file) -> str:
    input_line = get_input_line(input_file)

    return solve(input_line, True)


if __name__ == '__main__':
    answer = puzzle1("../resources/y2020/day23/day23_1.txt")
    print(answer)

    answer = puzzle1("../resources/y2020/day23/day23_2.txt")
    print(answer)

    answer = puzzle2("../resources/y2020/day23/day23_1.txt")
    print(answer)

    answer = puzzle2("../resources/y2020/day23/day23_2.txt")
    print(answer)
