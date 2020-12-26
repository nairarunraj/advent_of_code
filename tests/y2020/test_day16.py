import unittest

from y2020.day16 import puzzle1, puzzle2


class TestsDay16(unittest.TestCase):
    def test_puzzle1_sample(self):
        answer = puzzle1("../../resources/y2020/day16/day16_1.txt")
        self.assertEqual(71, answer)

    def test_puzzle1_challenge(self):
        answer = puzzle1("../../resources/y2020/day16/day16_2.txt")
        self.assertEqual(19240, answer)

    def test_puzzle2_sample(self):
        answer = puzzle2("../../resources/y2020/day16/day16_3.txt")
        self.assertEqual(1, answer)

    def test_puzzle2_challenge(self):
        answer = puzzle2("../../resources/y2020/day16/day16_2.txt")
        self.assertEqual(21095351239483, answer)


if __name__ == '__main__':
    unittest.main()
