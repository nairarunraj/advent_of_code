"""
--- Day 25: Combo Breaker ---
"""

from y2020.file_utils import get_input_data


def puzzle1(input_file) -> int:
    input_content = get_input_data(input_file)

    card_pub_key = int(input_content[0])
    door_pub_key = int(input_content[1])

    loop_sizes = {}
    subject_no = 7
    loop_size = 0
    public_key = 1
    while True:
        if len(loop_sizes) == 2:
            break

        if public_key == card_pub_key:
            loop_sizes['card'] = loop_size

        if public_key == door_pub_key:
            loop_sizes['door'] = loop_size

        public_key *= subject_no
        public_key %= 20201227

        loop_size += 1

    subject_no = door_pub_key
    public_key = 1
    for _ in range(loop_sizes['card']):
        public_key *= subject_no
        public_key %= 20201227

    return public_key


if __name__ == '__main__':
    answer = puzzle1("../resources/y2020/day25/day25_1.txt")
    print(answer)

    answer = puzzle1("../resources/y2020/day25/day25_2.txt")
    print(answer)
