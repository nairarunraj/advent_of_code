import unittest

from y2020.day15 import puzzle1, puzzle2


class TestsDay15(unittest.TestCase):
    def test_puzzle1_sample(self):
        answer = puzzle1("../../resources/y2020/day15/day15_1.txt", 2020)
        self.assertEqual(436, answer)

    def test_puzzle1_challenge(self):
        answer = puzzle1("../../resources/y2020/day15/day15_2.txt", 2020)
        self.assertEqual(1522, answer)

    def test_puzzle2_sample(self):
        answer = puzzle2("../../resources/y2020/day15/day15_1.txt", 30000000)
        self.assertEqual(175594, answer)

    def test_puzzle2_challenge(self):
        answer = puzzle2("../../resources/y2020/day15/day15_2.txt", 30000000)
        self.assertEqual(18234, answer)


if __name__ == '__main__':
    unittest.main()
