import unittest

from y2020.day11 import puzzle1, puzzle2


class TestsDay11(unittest.TestCase):
    def test_puzzle1_sample(self):
        answer = puzzle1("../../resources/y2020/day11/day11_1.txt")
        self.assertEqual(37, answer)

    def test_puzzle1_challenge(self):
        answer = puzzle1("../../resources/y2020/day11/day11_2.txt")
        self.assertEqual(2273, answer)

    def test_puzzle2_sample(self):
        answer = puzzle2("../../resources/y2020/day11/day11_1.txt")
        self.assertEqual(26, answer)

    def test_puzzle2_challenge(self):
        answer = puzzle2("../../resources/y2020/day11/day11_2.txt")
        self.assertEqual(2064, answer)


if __name__ == '__main__':
    unittest.main()
