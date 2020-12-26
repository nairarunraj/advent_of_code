import unittest

from y2020.day13 import puzzle1, puzzle2


class TestsDay13(unittest.TestCase):
    def test_puzzle1_sample(self):
        answer = puzzle1("../../resources/y2020/day13/day13_1.txt")
        self.assertEqual(295, answer)

    def test_puzzle1_challenge(self):
        answer = puzzle1("../../resources/y2020/day13/day13_2.txt")
        self.assertEqual(3966, answer)

    def test_puzzle2_sample(self):
        answer = puzzle2("../../resources/y2020/day13/day13_1.txt")
        self.assertEqual(1068781, answer)

    def test_puzzle2_challenge(self):
        answer = puzzle2("../../resources/y2020/day13/day13_2.txt")
        self.assertEqual(800177252346225, answer)


if __name__ == '__main__':
    unittest.main()
