"""
--- Day 12: Rain Risk ---
"""

from y2020.file_utils import get_input_data


def puzzle1(input_file) -> int:
    input_content = get_input_data(input_file)

    x_pos = 0
    y_pos = 0
    direction = 0
    direction_x = (1, 0, -1, 0)
    direction_y = (0, -1, 0, 1)
    for instr in input_content:
        (cmd, value) = (instr[0], int(instr[1:]))

        if cmd == 'F':
            x_pos += (value * direction_x[direction])
            y_pos += (value * direction_y[direction])

        elif cmd == 'R':
            direction = (direction + int(value / 90)) % 4

        elif cmd == 'L':
            direction = (direction + int(value / 90) * 3) % 4

        elif cmd == 'N':
            y_pos += value

        elif cmd == 'S':
            y_pos -= value

        elif cmd == 'E':
            x_pos += value

        elif cmd == 'W':
            x_pos -= value

    return abs(x_pos) + abs(y_pos)


def puzzle2(input_file) -> int:
    input_content = get_input_data(input_file)

    x_pos = 0
    y_pos = 0
    waypoint_rel_x = waypoint_x = 10
    waypoint_rel_y = waypoint_y = 1
    for instr in input_content:
        (cmd, value) = (instr[0], int(instr[1:]))

        if cmd == 'F':
            ship_x = waypoint_rel_x * value
            ship_y = waypoint_rel_y * value
            x_pos += ship_x
            y_pos -= ship_y

            waypoint_x = x_pos + waypoint_rel_x
            waypoint_y = x_pos + waypoint_rel_y

        if cmd == 'R':
            if value == 90:
                waypoint_x = x_pos + waypoint_rel_y
                waypoint_y = y_pos - waypoint_rel_x

            if value == 180:
                waypoint_x = x_pos - waypoint_rel_x
                waypoint_y = y_pos - waypoint_rel_y

            if value == 270:
                waypoint_x = x_pos - waypoint_rel_y
                waypoint_y = y_pos + waypoint_rel_x

            waypoint_rel_x = waypoint_x - x_pos
            waypoint_rel_y = waypoint_y - y_pos

        if cmd == 'L':
            if value == 270:
                waypoint_x = x_pos + waypoint_rel_y
                waypoint_y = y_pos - waypoint_rel_x

            if value == 180:
                waypoint_x = x_pos - waypoint_rel_x
                waypoint_y = y_pos - waypoint_rel_y

            if value == 90:
                waypoint_x = x_pos - waypoint_rel_y
                waypoint_y = y_pos + waypoint_rel_x

            waypoint_rel_x = waypoint_x - x_pos
            waypoint_rel_y = waypoint_y - y_pos

        if cmd == 'N':
            waypoint_rel_y += value
            waypoint_y = y_pos + waypoint_rel_y

        if cmd == 'S':
            waypoint_rel_y -= value
            waypoint_y = y_pos + waypoint_rel_y

        if cmd == 'E':
            waypoint_rel_x += value
            waypoint_x = x_pos + waypoint_rel_x

        if cmd == 'W':
            waypoint_rel_x -= value
            waypoint_x = y_pos + waypoint_rel_x

    return abs(x_pos) + abs(y_pos)


if __name__ == '__main__':
    answer = puzzle1("../../resources/y2020/day12/day12_1.txt")
    print(answer)

    answer = puzzle1("../../resources/y2020/day12/day12_2.txt")
    print(answer)

    answer = puzzle2("../../resources/y2020/day12/day12_1.txt")
    print(answer)

    answer = puzzle2("../../resources/y2020/day12/day12_2.txt")
    print(answer)
