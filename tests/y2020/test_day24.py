import unittest

from y2020.day24 import puzzle1, puzzle2


class TestsDay24(unittest.TestCase):
    def test_puzzle1_sample(self):
        answer = puzzle1("../../resources/y2020/day24/day24_1.txt")
        self.assertEqual(10, answer)

    def test_puzzle1_challenge(self):
        answer = puzzle1("../../resources/y2020/day24/day24_2.txt")
        self.assertEqual(377, answer)

    def test_puzzle2_sample(self):
        answer = puzzle2("../../resources/y2020/day24/day24_1.txt")
        self.assertEqual(2208, answer)

    def test_puzzle2_challenge(self):
        answer = puzzle2("../../resources/y2020/day24/day24_2.txt")
        self.assertEqual(4231, answer)


if __name__ == '__main__':
    unittest.main()
