import unittest

from y2020.day4 import puzzle1, puzzle2


class TestsDay4(unittest.TestCase):
    def test_puzzle1_sample(self):
        answer = puzzle1("../../resources/y2020/day4/day4_1.txt")
        self.assertEqual(2, answer)

    def test_puzzle1_challenge(self):
        answer = puzzle1("../../resources/y2020/day4/day4_2.txt")
        self.assertEqual(210, answer)

    def test_puzzle2_sample(self):
        answer = puzzle2("../../resources/y2020/day4/day4_1.txt")
        self.assertEqual(2, answer)

    def test_puzzle2_challenge(self):
        answer = puzzle2("../../resources/y2020/day4/day4_2.txt")
        self.assertEqual(131, answer)


if __name__ == '__main__':
    unittest.main()
