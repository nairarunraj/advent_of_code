import unittest

from y2020.day5 import puzzle1, puzzle2


class TestsDay5(unittest.TestCase):
    def test_puzzle1_sample(self):
        answer = puzzle1("../../resources/y2020/day5/day5_1.txt")
        self.assertEqual(820, answer)

    def test_puzzle1_challenge(self):
        answer = puzzle1("../../resources/y2020/day5/day5_2.txt")
        self.assertEqual(855, answer)

    def test_puzzle2_challenge(self):
        answer = puzzle2("../../resources/y2020/day5/day5_2.txt")
        self.assertEqual(552, answer)


if __name__ == '__main__':
    unittest.main()
