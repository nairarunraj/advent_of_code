import unittest

from y2020.day3 import puzzle1, puzzle2


class TestsDay3(unittest.TestCase):
    def test_puzzle1_sample(self):
        answer = puzzle1("../../resources/y2020/day3/day3_1.txt")
        self.assertEqual(7, answer)

    def test_puzzle1_challenge(self):
        answer = puzzle1("../../resources/y2020/day3/day3_2.txt")
        self.assertEqual(173, answer)

    def test_puzzle2_sample(self):
        answer = puzzle2("../../resources/y2020/day3/day3_1.txt")
        self.assertEqual(336, answer)

    def test_puzzle2_challenge(self):
        answer = puzzle2("../../resources/y2020/day3/day3_2.txt")
        self.assertEqual(4385176320, answer)


if __name__ == '__main__':
    unittest.main()
