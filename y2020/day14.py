"""
--- Day 14: Docking Data ---
"""

from y2020.file_utils import get_input_data


def modify_bit(addr, idx, bit_val):
    mask = 1 << idx  # 1 at pos idx, rest are 0's
    # ~mask => 0 at pos idx, rest are 1's

    # addr having 0 at pos idx OR'd with bit_val at pos idx
    return (addr & ~mask) | (bit_val << idx)


def puzzle1(input_file) -> int:
    input_content = get_input_data(input_file)

    mask = {}
    memory = {}
    for line in input_content:
        if line.startswith("mask"):
            mask = {}
            (_, mask_val) = line.split(" = ")
            for idx, mask_bit in enumerate(reversed(mask_val)):
                if mask_bit != 'X':
                    mask[int(idx)] = int(mask_bit)

            continue

        (mem, val_str) = line.split(" = ")
        mem_val = int(mem[4:-1])
        val = int(val_str)
        result_val = val
        for idx, mask_bit in sorted(mask.items()):
            result_val = modify_bit(result_val, idx, mask_bit)

        memory[mem_val] = result_val

    return sum(memory.values())


def modify_floating_bit(mem_val, mask_x, addresses, idx):
    if idx == len(mask_x):
        return addresses

    modified_addr = modify_bit(mem_val, mask_x[idx], 0)
    addresses.add(modified_addr)
    addresses = modify_floating_bit(modified_addr, mask_x, addresses, idx + 1)

    modified_addr = modify_bit(mem_val, mask_x[idx], 1)
    addresses.add(modified_addr)
    addresses = modify_floating_bit(modified_addr, mask_x, addresses, idx + 1)

    return addresses


def puzzle2(input_file) -> int:
    input_content = get_input_data(input_file)

    mask = {}
    mask_x = {}
    memory = {}
    for line in input_content:
        if line.startswith("mask"):
            mask = {}
            mask_x = []
            (_, mask_val) = line.split(" = ")
            for idx, mask_bit in enumerate(reversed(mask_val)):
                if mask_bit == 'X':
                    mask_x.append(int(idx))
                    continue

                mask[int(idx)] = int(mask_bit)

            continue

        (mem, val_str) = line.split(" = ")
        mem_val = int(mem[4:-1])
        val = int(val_str)

        result_addr = mem_val
        for idx, mask_bit in sorted(mask.items()):
            if mask_bit == 0:
                continue
            result_addr = modify_bit(result_addr, idx, mask_bit)

        addresses = {result_addr}
        addresses = modify_floating_bit(result_addr, mask_x, addresses, 0)
        for addr in addresses:
            memory[addr] = val

    return sum(memory.values())


if __name__ == '__main__':
    answer = puzzle1("../resources/y2020/day14/day14_1.txt")
    print(answer)

    answer = puzzle1("../resources/y2020/day14/day14_2.txt")
    print(answer)

    answer = puzzle2("../resources/y2020/day14/day14_3.txt")
    print(answer)

    answer = puzzle2("../resources/y2020/day14/day14_2.txt")
    print(answer)
