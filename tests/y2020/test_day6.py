import unittest

from y2020.day6 import puzzle1, puzzle2


class TestsDay6(unittest.TestCase):
    def test_puzzle1_sample(self):
        answer = puzzle1("../../resources/y2020/day6/day6_1.txt")
        self.assertEqual(11, answer)

    def test_puzzle1_challenge(self):
        answer = puzzle1("../../resources/y2020/day6/day6_2.txt")
        self.assertEqual(6630, answer)

    def test_puzzle2_sample(self):
        answer = puzzle2("../../resources/y2020/day6/day6_1.txt")
        self.assertEqual(6, answer)

    def test_puzzle2_challenge(self):
        answer = puzzle2("../../resources/y2020/day6/day6_2.txt")
        self.assertEqual(3437, answer)


if __name__ == '__main__':
    unittest.main()
