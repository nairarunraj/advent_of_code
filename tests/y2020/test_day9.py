import unittest

from y2020.day9 import puzzle1, puzzle2


class TestsDay9(unittest.TestCase):
    def test_puzzle1_sample(self):
        answer = puzzle1("../../resources/y2020/day9/day9_1.txt", 5)
        self.assertEqual(127, answer)

    def test_puzzle1_challenge(self):
        answer = puzzle1("../../resources/y2020/day9/day9_2.txt", 25)
        self.assertEqual(542529149, answer)

    def test_puzzle2_sample(self):
        answer = puzzle2("../../resources/y2020/day9/day9_1.txt", 5)
        self.assertEqual(62, answer)

    def test_puzzle2_challenge(self):
        answer = puzzle2("../../resources/y2020/day9/day9_2.txt", 25)
        self.assertEqual(75678618, answer)


if __name__ == '__main__':
    unittest.main()
