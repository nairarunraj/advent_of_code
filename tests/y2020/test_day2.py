import unittest

from y2020.day2 import puzzle1, puzzle2


class TestsDay2(unittest.TestCase):

    def test_puzzle1_sample(self):
        answer = puzzle1("../../resources/y2020/day2/day2_1.txt")
        self.assertEqual(2, answer)

    def test_puzzle1_challenge(self):
        answer = puzzle1("../../resources/y2020/day2/day2_2.txt")
        self.assertEqual(603, answer)

    def test_puzzle2_sample(self):
        answer = puzzle2("../../resources/y2020/day2/day2_1.txt")
        self.assertEqual(1, answer)

    def test_puzzle2_challenge(self):
        answer = puzzle2("../../resources/y2020/day2/day2_2.txt")
        self.assertEqual(404, answer)


if __name__ == '__main__':
    unittest.main()
