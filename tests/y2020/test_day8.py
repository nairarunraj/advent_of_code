import unittest

from y2020.day8 import puzzle1, puzzle2


class TestsDay8(unittest.TestCase):
    def test_puzzle1_sample(self):
        answer = puzzle1("../../resources/y2020/day8/day8_1.txt")
        self.assertEqual(5, answer)

    def test_puzzle1_challenge(self):
        answer = puzzle1("../../resources/y2020/day8/day8_2.txt")
        self.assertEqual(1594, answer)

    def test_puzzle2_sample(self):
        answer = puzzle2("../../resources/y2020/day8/day8_1.txt")
        self.assertEqual(8, answer)

    def test_puzzle2_challenge(self):
        answer = puzzle2("../../resources/y2020/day8/day8_2.txt")
        self.assertEqual(758, answer)


if __name__ == '__main__':
    unittest.main()
