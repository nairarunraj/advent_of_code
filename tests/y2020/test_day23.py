import unittest

from y2020.day23 import puzzle1, puzzle2


class TestsDay23(unittest.TestCase):
    def test_puzzle1_sample(self):
        answer = puzzle1("../../resources/y2020/day23/day23_1.txt")
        self.assertEqual('67384529', answer)

    def test_puzzle1_challenge(self):
        answer = puzzle1("../../resources/y2020/day23/day23_2.txt")
        self.assertEqual('24987653', answer)

    def test_puzzle2_sample(self):
        answer = puzzle2("../../resources/y2020/day23/day23_1.txt")
        self.assertEqual(149245887792, answer)

    def test_puzzle2_challenge(self):
        answer = puzzle2("../../resources/y2020/day23/day23_2.txt")
        self.assertEqual(442938711161, answer)


if __name__ == '__main__':
    unittest.main()
