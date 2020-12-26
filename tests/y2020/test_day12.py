import unittest

from y2020.day12 import puzzle1, puzzle2


class TestsDay12(unittest.TestCase):
    def test_puzzle1_sample(self):
        answer = puzzle1("../../resources/y2020/day12/day12_1.txt")
        self.assertEqual(25, answer)

    def test_puzzle1_challenge(self):
        answer = puzzle1("../../resources/y2020/day12/day12_2.txt")
        self.assertEqual(636, answer)

    def test_puzzle2_sample(self):
        answer = puzzle2("../../resources/y2020/day12/day12_1.txt")
        self.assertEqual(286, answer)

    def test_puzzle2_challenge(self):
        answer = puzzle2("../../resources/y2020/day12/day12_2.txt")
        self.assertEqual(26841, answer)


if __name__ == '__main__':
    unittest.main()
