"""
--- Day 8: Handheld Halting ---
"""

from y2020.file_utils import get_input_data


def puzzle1(input_file) -> int:
    input_content = get_input_data(input_file)

    current_index = 0
    visited = {}
    accumulator = 0
    while True:
        if current_index == len(input_content):
            return accumulator

        if current_index in visited:
            return accumulator

        instruction = input_content[current_index]
        (op, offset) = instruction.split(' ')
        direction = offset[0]
        offset_val = int(offset[1:])

        visited[current_index] = 1

        multiplier = 1
        if direction == '-': multiplier = -1

        if op == 'acc': accumulator += (multiplier * offset_val)

        if op in ('nop', 'acc'):
            current_index += 1
            continue

        if op == 'jmp':
            current_index += (multiplier * offset_val)

    return accumulator


def execute_instr(instr_set, current_index, op_changed, accumulator, visited):
    if current_index == len(instr_set):
        return accumulator

    if current_index in visited:
        return None

    instr_row = instr_set[current_index]
    (op, offset) = instr_row.split(' ')
    direction = offset[0]
    offset_val = int(offset[1:])

    multiplier = 1
    if direction == '-': multiplier = -1

    visited[current_index] = 1

    if op == 'acc':
        accumulator += (multiplier * offset_val)
        return execute_instr(instr_set, current_index + 1, op_changed, accumulator, visited)

    if op == 'nop':
        if op_changed:
            return execute_instr(instr_set, current_index + 1, op_changed, accumulator, visited)

        no_op_change_acc = execute_instr(instr_set, current_index + 1, op_changed, accumulator, visited)
        if no_op_change_acc is not None:
            return no_op_change_acc

        new_index = current_index + (multiplier * offset_val)
        return execute_instr(instr_set, new_index, True, accumulator, visited)

    if op == 'jmp':
        new_index = current_index + (multiplier * offset_val)

        if op_changed:
            return execute_instr(instr_set, new_index, op_changed, accumulator, visited)

        no_op_change_acc = execute_instr(instr_set, new_index, op_changed, accumulator, visited)
        if no_op_change_acc is not None:
            return no_op_change_acc

        return execute_instr(instr_set, current_index + 1, True, accumulator, visited)


def puzzle2(input_file) -> int:
    input_content = get_input_data(input_file)

    return execute_instr(input_content, 0, False, 0, {})


if __name__ == '__main__':
    answer = puzzle1("../../resources/y2020/day8/day8_1.txt")
    print(answer)

    answer = puzzle1("../../resources/y2020/day8/day8_2.txt")
    print(answer)

    answer = puzzle2("../../resources/y2020/day8/day8_1.txt")
    print(answer)

    answer = puzzle2("../../resources/y2020/day8/day8_2.txt")
    print(answer)
